from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from Hql.Config import Config
    from Hql.Data import Data

class QueryPool():
    def __init__(self, auto_run:bool=True) -> None:
        self.auto_run = auto_run
        self.pool:list[QueryThread] = []

    def add_query(self, text:str, config:'Config', name:str='', **kwargs) -> None:
        t = QueryThread(text, config, name=name, **kwargs)
        t.start()
        self.pool.append(t)

    def is_idle(self) -> bool:
        return not self.pool

    # Gets completed threads and frees them from the pool
    def get_completed(self) -> list['QueryThread']:
        completed = []
        for t in self.pool:
            if not t.is_alive():
                t.join()
                completed.append(t)
                self.pool.remove(t)
        return completed

class QueryThread():
    def __init__(self, text:str, config:'Config', name:str='', **kwargs) -> None:
        from copy import deepcopy
        from Hql.Helpers import can_thread

        self.text = text
        self.config = deepcopy(config)
        self.name = name
        self.threaded = can_thread()
        self.kwargs = kwargs

        self.thread = None
        self.output = None
        self.failed = False

    # Starts the thread and sets values in the class
    def start(self) -> None:
        if not self.threaded:
            self.run()
            return

        from threading import Thread
        self.thread = Thread(name=self.name, target=self.run, args=())
        self.thread.start()

    # Runs the query, function that is threaded
    def run(self) -> None:
        from Hql.Helpers import run_query
        try:
            self.output = run_query(self.text, self.config, name=self.name, **self.kwargs)
        except Exception as e:
            import traceback
            self.failed = True
            self.output = traceback.format_exc()

    def is_alive(self) -> bool:
        if not self.thread or not self.threaded:
            return False
        return self.thread.is_alive()

    def join(self) -> Union['Data', str, None]:
        if self.threaded and self.thread:
            self.thread.join()
        return self.output

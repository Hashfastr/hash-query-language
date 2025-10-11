from typing import TYPE_CHECKING, Union, Optional
import logging

if TYPE_CHECKING:
    from Hql.Config import Config
    from Hql.Data import Data
    from Hql.Operators import Database
    from Hql.Compiler import InstructionSet
    from Hql.Context import Context
    from Hql.Hac.Engine import Detection

class QueryPool():
    def __init__(self, auto_run:bool=True) -> None:
        self.auto_run = auto_run
        self.pool:list[QueryThread] = []

    def add_query(self, text:str, config:'Config', name:str='', **kwargs) -> None:
        t = QueryThread(text, config, name=name, **kwargs)
        if self.auto_run:
            t.start()
        self.pool.append(t)

    def is_idle(self) -> bool:
        return not self.pool

    def start(self):
        for t in self.pool:
            if not t.started:
                t.start()

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

        self.started = False
        self.thread = None
        self.output = None
        self.failed = False

    # Starts the thread and sets values in the class
    def start(self) -> None:
        self.started = True

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

class InstructionPool():
    def __init__(self, auto_run:bool=True) -> None:
        self.auto_run = auto_run
        self.pool:list[InstructionThread] = []

    def add_instruction(self, inst:Union['InstructionSet', 'Database'], ctx:'Context') -> None:
        t = InstructionThread(inst, ctx)
        if self.auto_run:
            t.start()
        self.pool.append(t)

    def is_idle(self) -> bool:
        return not self.pool

    def start(self):
        # Don't thread if we don't need to
        if len(self.pool) == 1:
            self.pool[0].run()
            return

        for t in self.pool:
            if not t.started:
                t.start()

    # Gets completed threads and frees them from the pool
    def get_completed(self) -> list['InstructionThread']:
        completed = []
        for t in self.pool:
            if not t.is_alive():
                t.join()
                completed.append(t)
                self.pool.remove(t)
        return completed

class InstructionThread():
    def __init__(self, inst:Union['InstructionSet', 'Database'], ctx:'Context') -> None:
        from copy import deepcopy
        from Hql.Helpers import can_thread

        self.threaded = can_thread()

        self.inst = inst
        self.ctx = ctx
        self.started = False
        self.thread = None
        self.output:Optional['Context'] = None

    # Starts the thread and sets values in the class
    def start(self) -> None:
        if not self.threaded:
            self.run()
            return

        from threading import Thread
        self.thread = Thread(name=self.inst.id, target=self.run, args=())
        self.thread.start()

    # Runs the query, function that is threaded
    def run(self) -> None:
        from Hql.Data import Data
        from Hql.Context import Context

        out = self.inst.eval(self.ctx)
        if isinstance(out, Data):
            out = Context(out)
        self.output = out

    def is_alive(self) -> bool:
        if not self.thread or not self.threaded:
            return False
        return self.thread.is_alive()

    def join(self) -> Optional['Context']:
        if self.threaded and self.thread:
            self.thread.join()
        return self.output

class HacPool():
    def __init__(self, auto_run:bool=True) -> None:
        self.auto_run = auto_run
        self.pool:list[HacThread] = []

    def add_detection(self, detection:'Detection') -> None:
        t = HacThread(detection)
        if self.auto_run:
            t.start()
        self.pool.append(t)

    def is_idle(self) -> bool:
        return not self.pool

    def start(self):
        for t in self.pool:
            if not t.started:
                t.start()

    # Gets completed threads and frees them from the pool
    def get_completed(self) -> list['HacThread']:
        completed = []
        for t in self.pool:
            if not t.is_alive():
                t.join()
                completed.append(t)
                self.pool.remove(t)
        return completed

class HacThread():
    def __init__(self, detection:'Detection') -> None:
        from Hql.Helpers import can_thread
        self.threaded = can_thread()

        self.detection = detection

        self.started = False
        self.thread = None
        self.output = None
        self.failed = False

    # Starts the thread and sets values in the class
    def start(self) -> None:
        self.started = True
        logging.info(f'Starting detection {self.detection.id}')

        if not self.threaded:
            self.run()
            return

        from threading import Thread
        self.thread = Thread(name=self.detection.id, target=self.run, args=())
        self.thread.start()

    # Runs the query, function that is threaded
    def run(self) -> None:
        try:
            self.output = self.detection.run()
            logging.info(f'{self.detection.id} - {len(self.output)} results')
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

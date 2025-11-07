from typing import TYPE_CHECKING, Union, Optional
import logging
import random
import datetime, time

if TYPE_CHECKING:
    from Hql.Config import Config
    from Hql.Data import Data
    from Hql.Operators import Database
    from Hql.Compiler import InstructionSet
    from Hql.Context import Context
    from Hql.Hac.Engine import Detection

class QueryPool():
    def __init__(self, auto_run:bool=True) -> None:
        from threading import Semaphore
        self.auto_run = auto_run
        self.pool:list[QueryThread] = []
        self.semaphore = Semaphore()

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
        from threading import Semaphore
        self.auto_run = auto_run
        self.pool:list[InstructionThread] = []
        self.semaphore = Semaphore()

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
            instid = self.pool[0].id
            logging.debug(f'No need to thread {instid}, only one instruction in the pool')
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
        self.id = self.inst.id

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
        import copy

        out = self.inst.eval(self.ctx)
        if isinstance(out, Data):
            ctx = copy.deepcopy(self.ctx)
            ctx.data = out
            out = ctx
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
        from threading import Semaphore
        self.auto_run = auto_run
        self.pool:list[HacThread] = []
        self.queue:list[HacThread] = []
        self.semaphore = Semaphore(16)

        self.completed:list[HacThread] = []
        self.max_retained = 1000

    def get_by_id(self, tid:str):
        for i in self.pool + self.completed + self.queue:
            if i.id == tid:
                return i
        return None

    def get_runs(self):
        runs = []
        for i in self.pool:
            runs.append({
                'run_id': i.id,
                'run_date': i.run_date.isoformat(),
                'started': i.started,
                'failed': i.failed,
                'completed': i.completed
            })
        return runs

    def add_detection(self, detection:'Detection', query_now:Optional[datetime.datetime]=None) -> str:
        t = HacThread(detection, query_now=query_now)
        if self.auto_run and self.semaphore.acquire(blocking=False):
            logging.debug(f'{t.id} started execution')
            t.start()
            self.pool.append(t)
        else:
            logging.debug(f'{t.id} queued for execution')
            self.queue.append(t)

        return t.id

    def is_idle(self) -> bool:
        return not self.pool

    def clear_queue(self):
        count = 0
        for t in self.queue:
            if self.semaphore.acquire(blocking=False):
                self.pool.append(t)
                self.queue.remove(t)
                t.start()
                count += 1
            else:
                break
        if count:
            logging.debug(f'Moved {count} detections from queue to running')

    def gather_threads(self):
        for t in self.pool:
            if not t.is_alive():
                t.join()
                self.pool.remove(t)
                self.semaphore.release()

                if len(self.completed) >= self.max_retained:
                    self.completed = self.completed[1:]
                self.completed.append(t)

    def get_completed(self) -> list['HacThread']:
        completed = self.completed
        self.completed = []
        return completed

class HacThread():
    def __init__(self, detection:'Detection', query_now:Optional[datetime.datetime]=None) -> None:
        from Hql.Helpers import can_thread
        self.threaded = can_thread()

        self.query_now = query_now if query_now else datetime.datetime.now()
        self.detection = detection

        self.started = False
        self.completed = False
        self.thread = None
        self.output = None
        self.failed = False
        self.num_results = 0

        self.id = '%08x' % random.getrandbits(32)
        self.run_date = datetime.datetime.now()
        self.duration = 0

    def to_dict(self):
        from Hql.Data import Data
        d = {
            'run_id': self.id,
            'run_date': self.run_date.isoformat(),
            'started': self.started,
            'duration': self.duration,
            'failed': self.failed,
            'completed': self.completed,
            'num_results': self.num_results
        }

        if self.detection.hac:
            d['hac'] = self.detection.hac.asm

        d['results'] = self.output.to_dict() if isinstance(self.output, Data) else {}
        d['str_out'] = self.output if isinstance(self.output, str) else ''

        return d

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
        from Hql.Data import Data
        try:
            start = time.perf_counter()
            self.output = self.detection.run()
            end = time.perf_counter()
            
            self.duration = end - start
            self.completed = True
            self.num_results = len(self.output) if isinstance(self.output, Data) else 0

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

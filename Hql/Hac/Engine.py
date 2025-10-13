from typing import TYPE_CHECKING, Optional
from Hql.Exceptions import HacExceptions as hace
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Compiler import InstructionSet
from pathlib import Path
import datetime
import logging

if TYPE_CHECKING:
    from Hql.Config import Config
    from Hql.Hac import Hac
    from Hql.Parser import SigmaParser
    from Hql.Data import Data
    from Hql.Compiler import HqlCompiler

class CronException(Exception):
    def __init__(self, message:str=""):
        self.type = self.__class__.__name__
        Exception.__init__(self, f"Invalid cron schedule {message}")

class Schedule():
    def __init__(self, cronstr:str) -> None:
        self.cronstr = cronstr
        self.last_fired = 0
        self.weekdays = ['sun', 'mon', 'tues', 'wed', 'thu', 'fri', 'sat']
        self.bounds = {
            'minutes':  (0, 59),
            'hours':    (0, 23),
            'days':     (1, 31),
            'months':   (1, 12),
            'weekdays': (0, 6)
        }
        self.schedule:tuple[set, set, set, set, set] = self.parse_cron(cronstr)

    def should_fire(self, time_parts:tuple[int, int, int, int, int]):
        for i in range(5):
            if time_parts[i] not in self.schedule[i]:
                return False
        return True

    def parse_cron(self, cronstr:str) -> tuple[set, set, set, set, set]:
        parts = cronstr.split(' ')

        for p in parts:
            if not p:
                parts.remove(p)
        
        minutes = self.parse_part(parts[0], 'minutes')
        hours = self.parse_part(parts[1], 'hours')
        months = self.parse_part(parts[2], 'months')
        days = self.parse_part(parts[3], 'days')
        weekdays = self.parse_part(parts[4], 'weekdays')

        return (minutes, hours, months, days, weekdays)

    def parse_part(self, part:str, kind:str) -> set[int]:
        out_set:set[int] = set()
        opts = part.split(',')

        for i in opts:
            interval = 0
            value = i
            if len(i.split('/')) > 1:
                interval = i.split('/')[1]
                value = i.split('/')[0]

                try:
                    interval = int(interval)
                except ValueError:
                    raise CronException(f'Invalid cron schedule {self.cronstr}')
            
            start = value
            end = ''
            if len(start.split('-')) > 1:
                end = start.split('-')[1]
                start = start.split('-')[0]

            if end and ('*' in start or '*' in end):
                raise CronException(f'Invalid cron schedule {self.cronstr}')

            if kind == 'weekdays':
                if start in self.weekdays:
                    start = self.weekdays.index(start)
                if end in self.weekdays:
                    end = self.weekdays.index(end)

            try:
                if not isinstance(start, int) and start != '*':
                    start = int(start)
                if end and not isinstance(end, int):
                    end = int(end)
            except ValueError:
                raise Exception(f'Invalid cron schedule {self.cronstr}')

            bot, top = self.bounds[kind]
            if not end and interval:
                end = top

            if start != '*':
                if (start < bot or start > top):
                    raise CronException(self.cronstr)

                if end and (end < start or end < bot or end > top):
                    raise CronException(self.cronstr)

            if not interval:
                if start == '*':
                    [out_set.add(x) for x in range(bot, top + 1)]
                elif end:
                    [out_set.add(x) for x in range(start, end + 1)]
                else:
                    out_set.add(start)

            else:
                assert start != '*'
                if end:
                    [out_set.add(x) for x in range(start, end + 1, interval)]
                else:
                    [out_set.add(x) for x in range(start, top + 1, interval)]

        return out_set

class Detection():
    def __init__(self, txt:str, src:str, config:'Config') -> None:
        self.src = src
        self.txt = txt
        self.config = config
        self.hac, self.parser = self.gen_hac()
        self.compiler = None
        self.schedule = None
        self.id = ''

        # skip instruction compiling if we don't have hac
        if self.hac:
            self.id = self.hac.id
            self.compiler = self.compile()
            self.schedule = Schedule(self.hac.schedule)

    def gen_hac(self) -> tuple[Optional['Hac'], Optional['SigmaParser']]:
        from Hql.Hac import Parser as HaCParser
        from Hql.Parser import SigmaParser

        parser = None
        hac = None

        try:
            parser = SigmaParser(self.txt)
            hac = parser.gen_hac()
        except Exception:
            # We're just skipping over to HaC Parsing then
            try:
                hac = HaCParser.parse_text(self.txt, self.src)
            except (hace.LexerException, hace.HacException):
                hac = None

        return hac, parser

    def compile(self) -> 'HqlCompiler':
        from Hql.Parser import Parser
        from Hql.Query import Query
        from Hql.Compiler import HqlCompiler

        if not self.parser:
            self.parser = Parser(self.txt, self.src)
        self.parser.assemble()
    
        if not isinstance(self.parser.assembly, Query):
            raise hqle.CompilerException(f'Attempting to compile non-Query assembly {type(self.parser.assembly)}')

        comp = HqlCompiler(self.config, self.parser.assembly)
        return comp

    def should_fire(self, time_parts:tuple[int, int, int, int, int]):
        if not self.schedule:
            return False
        return self.schedule.should_fire(time_parts)

    def run(self) -> 'Data':
        if not self.compiler:
            raise Exception('Attempting to run detection without instructions!')
        ctx = self.compiler.run()
        return ctx.data

class HacEngine():
    def __init__(self, path:Path, directory:bool, conf_path:Path, tz:Optional[datetime.tzinfo]=None) -> None:
        from Hql.Threading import HacPool

        self.path = path
        self.directory = directory
        self.files:list[Path] = self.scan_files()
        self.conf_path = conf_path
        self.config = self.load_conf()
        self.detections = self.load_files()
        self.tz = tz

        self.pool = HacPool()

    def time_parts(self, ts:int) -> tuple[int, int, int, int, int]:
        dt = datetime.datetime.fromtimestamp(ts, tz=self.tz)
        return (dt.minute, dt.hour, dt.month, dt.day, dt.weekday())

    def load_conf(self):
        from Hql.Config import Config
        return Config(self.conf_path)

    def scan_files(self) -> list[Path]:
        files = []

        if self.directory:
            # Hql
            for file in self.path.rglob('*.hql'):
                if file.is_file():
                    files.append(file)
            # yml
            for file in self.path.rglob('*.yml'):
                if file.is_file():
                    files.append(file)
        else:
            files.append(self.path)

        return files

    def load_files(self) -> list[Detection]:
        detections = []

        for i in self.files:
            with open(i, mode='r') as f:
                txt = f.read()    
            detections.append(Detection(txt, str(i), self.config))

        logging.info(f'HaC engine found {len(detections)} detections')

        return detections

    def wait_till(self, stamp:int, pad:int=0):
        from time import sleep
        cur = datetime.datetime.now(tz=self.tz).timestamp()
        if stamp <= cur:
            return
        delta = (stamp - cur) - pad
        sleep(delta)

    def run(self):
        logging.info(f'Starting HaC engine with {len(self.detections)} detections')

        while True:
            # adding 1 seconds for a time buffer
            dt = datetime.datetime.now(tz=self.tz) + datetime.timedelta(seconds=1)
            ts = dt.replace(second=0, microsecond=0) + datetime.timedelta(minutes=1)
            ts = int(ts.timestamp())
            self.wait_till(ts)

            for i in self.detections:
                if not i.should_fire(self.time_parts(ts)):
                    logging.debug(f'Skipping {i.id}, not their time')
                    continue
                self.pool.add_detection(i)

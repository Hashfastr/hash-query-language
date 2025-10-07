class HqlExceptions():
    class HqlException(Exception):
        def __init__(self, message:str=""):
            self.type = self.__class__.__name__
            Exception.__init__(self, f"{message}")

    class ConfigException(HqlException):
        def __init__(self, message:str="Config error occurred"):
            super().__init__(message)

    class SemanticException(HqlException):
        def __init__(self, message, line:int, charpos:int):
            super().__init__(f'{message}: line {line}:{charpos}')

    class FunctionException(HqlException):
        def __init__(self, message:str="Function error has occurred"):
            super().__init__(message)

    class ArgumentException(FunctionException):
        def __init__(self, message:str="Function argument error has occurred"):
            super().__init__(f"{message}")

    class LexerException(HqlException):
        def __init__(self, message:str, text:str, line:int, col:int, offsym:str, filename:str=''):
            self.text = text
            self.line = line
            self.col = col
            self.filename = filename
            
            HqlExceptions.HqlException.__init__(self, f'{message}: line {self.line}:{self.col}')

    class ParseException(HqlException):
        def __init__(self, message, ctx, filename:str=''):
            self.ctx = ctx
            self.line = ctx.start.line
            self.col = ctx.start.column
            self.filename = filename
            
            HqlExceptions.HqlException.__init__(self, f'{message}: line {self.line}:{self.col}')

    class CompilerException(HqlException):
        def __init__(self, message:str="A compiler error has occurred"):
            super().__init__(f"{message}")

    class QueryException(HqlException):
        def __init__(self, message:str="A query error has occurred"):
            super().__init__(f"{message}")

    class DecompileStringException(HqlException):
        def __init__(self, dtype:type, rtype:type):
            HqlExceptions.HqlException.__init__(self, f"Decompile for {dtype} returned non-str {rtype}")

###################
## HacExceptions ##
###################

class HacExceptions():
    class HacException(Exception):
        def __init__(self, message:str=""):
            self.type = self.__class__.__name__
            super().__init__(f"{self.type}: {message}")

    class ParseException(HacException):
        def __init__(self, message: str = ""):
            HacExceptions.HacException.__init__(self, f'{message}')

    class DagException(HacException):
        def __init__(self, name:str = '', message: str = ''):
            HacExceptions.HacException.__init__(self, f'{name}: {message}')

    class LexerException(HacException):
        def __init__(self, message:str, text:str, line:int, col:int, offsym:str, filename:str=''):
            self.text = text
            self.line = line
            self.col = col
            self.filename = filename
            
            HacExceptions.HacException.__init__(self, f'{message}: line {self.line}:{self.col}')

    class ActionException(HacException):
        def __init__(self, conf:dict, message: str = ""):
            message = f"{conf.get('action_name', conf['type'])} {message}"
            HacExceptions.HacException.__init__(self, message=message)

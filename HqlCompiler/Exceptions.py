class HqlException(Exception):
    def __init__(self, message:str=""):
        self.type = self.__class__.__name__
        super().__init__(f"{self.type}: {message}")

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
        
        HqlException.__init__(self, f'{message}: line {self.line}:{self.col}')

class ParseException(HqlException):
    def __init__(self, message, ctx, filename:str=''):
        self.ctx = ctx
        self.line = ctx.start.line
        self.col = ctx.start.column
        self.filename = filename
        
        HqlException.__init__(self, f'{message}: line {self.line}:{self.col}')

class CompilerException(HqlException):
    def __init__(self, message:str="A compiler error has occurred"):
        super().__init__(f"Compiler Exception: {message}")

class QueryException(HqlException):
    def __init__(self, message:str="A query error has occurred"):
        super().__init__(f"Query Exception: {message}")
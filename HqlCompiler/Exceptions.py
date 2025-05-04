class ConfigException(Exception):
    def __init__(self, message:str="Config error occurred"):
        super().__init__(message)

class SemanticException(Exception):
    def __init__(self, message, line:int, charpos:int):
        super().__init__(f'{message}: line {line}:{charpos}')

class FunctionException(Exception):
    def __init__(self, message:str="Function error has occurred"):
        super().__init__(message)

class ArgumentException(FunctionException):
    def __init__(self, message:str="Function argument error has occurred"):
        super().__init__(message)

class ParseException(Exception):
    def __init__(self, message, line:int, charpos:int):
        super().__init__(f'{message}: line {line}:{charpos}')
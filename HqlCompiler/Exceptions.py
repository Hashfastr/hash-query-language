class HqlException(Exception):
    def __init__(self, message:str=""):
        self.type = self.__class__.__name__
        super().__init__(f"{type}: {message}")

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

class ParseException(HqlException):
    def __init__(self, message, line:int, charpos:int):
        super().__init__(f'{message}: line {line}:{charpos}')

class CompilerException(HqlException):
    def __init__(self, message:str="A compiler error has occurred"):
        super().__init__(f"Compiler Exception: {message}")
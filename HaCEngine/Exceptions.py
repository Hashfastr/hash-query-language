class HaCException(Exception):
    def __init__(self, message:str=""):
        self.type = self.__class__.__name__
        super().__init__(f"{self.type}: {message}")

class ParseException(HaCException):
    def __init__(self, message: str = ""):
        HaCException.__init__(self, f'{message}')

class LexerException(HaCException):
    def __init__(self, message:str, text:str, line:int, col:int, offsym:str, filename:str=''):
        self.text = text
        self.line = line
        self.col = col
        self.filename = filename
        
        HaCException.__init__(self, f'{message}: line {self.line}:{self.col}')

class HacException(Exception):
    def __init__(self, message:str=""):
        self.type = self.__class__.__name__
        super().__init__(f"{self.type}: {message}")

class ParseException(HacException):
    def __init__(self, message: str = ""):
        HacException.__init__(self, f'{message}')

class DagException(HacException):
    def __init__(self, name:str = '', message: str = ''):
        HacException.__init__(self, f'{name}: {message}')

class LexerException(HacException):
    def __init__(self, message:str, text:str, line:int, col:int, offsym:str, filename:str=''):
        self.text = text
        self.line = line
        self.col = col
        self.filename = filename
        
        HacException.__init__(self, f'{message}: line {self.line}:{self.col}')

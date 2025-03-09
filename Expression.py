def getExpressionByName(name:str):
    if name == "nameReferenceWithDataScope":
        return scopedNameReference()

class Expression():
    def __init__(self):
        pass

class Equality(Expression):
    def __init__(self):
        super().__init__()
        pass

class scopedNameReference(Expression):
    def __init__(self):
        super().__init__()
        self.name = ''
        self.scope = ''
    
class stringLiteral(Expression):
    def __init__(self):
        super().__init__()
        pass
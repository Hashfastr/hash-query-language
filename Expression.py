import json

def getExpressionByName(name:str):
    if name == "nameReferenceWithDataScope":
        return scopedNameReference()

class Expression():
    def __init__(self):
        pass
    
    def to_dict(self):
        return {}
    
    def __str__(self):
        return json.dumps(self.__repr__(), indent=2)

class Equality(Expression):
    def __init__(self):
        super().__init__()
        

class scopedNameReference(Expression):
    def __init__(self, name:str, scope:str=""):
        super().__init__()
        self.name = name
        self.scope = scope
        
    def to_dict(self):
        return {
            'name': self.name,
            'scope': self.scope
        }
    
class stringLiteral(Expression):
    def __init__(self):
        super().__init__()
        pass
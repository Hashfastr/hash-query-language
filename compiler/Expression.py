import logging
import json

def getExpressionByName(name:str):
    if name == "nameReferenceWithDataScope":
        return ScopedNameReference()

class Expression():
    def __init__(self):
        pass
    
    def to_dict(self):
        return {}
    
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self) -> str:
        return self.__str__()

class Equality(Expression):
    def __init__(self, type:str=""):
        super().__init__()
        self.type = type
        self.expressions = []
    
    def to_dict(self):
        try:
            return {
                'type': self.type,
                'lh': self.expressions[0].to_dict(),
                'rh': self.expressions[1].to_dict()
            }
        except:
            for expression in self.expressions:
                print(expression)
            raise Exception("Failure to dict an equality")

class BetweenEquality(Expression):
    def __init__(self):
        super().__init__()
        self.expressions = []
        self.type = 'between'
    
    def to_dict(self):
        try:
            return {
                'type': self.type,
                'lh': self.expressions[0].to_dict(),
                'rh': {
                    'start': self.expressions[1].to_dict(),
                    'end': self.expressions[2].to_dict()
                }
            }
        except:
            for expression in self.expressions:
                print(expression)
            raise Exception("Failure to dict a between")

class ScopedNameReference(Expression):
    def __init__(self, name:str, scope:str=""):
        super().__init__()
        self.name = name
        self.scope = scope
        
    def to_dict(self):
        return {
            'name': self.name,
            'scope': self.scope
        }
    
class StringLiteral(Expression):
    def __init__(self, value:str):
        super().__init__()
        self.value = value.strip('"').strip("'")
        self.type = 'stringliteral'
        
    def get_name(self):
        return self.value
    
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }
        
class Integer(Expression):
    def __init__(self, value:str):
        super().__init__()
        self.value = int(value)
        self.type = 'integer'
        
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }
        
class RelationalExpression(Expression):
    def __init__(self):
        super().__init__()
        self.type = 'pipe'
import Expression
import json

class Operator():
    def __init__(self):
        self.type = ''
        self.expressions = []
    
    def to_dict(self):
        return {
            'type': self.type,
            'expressions':[x.to_dict() for x in self.expressions]
        }
    
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self):
        return self.__str__()

class Index(Operator):
    def __init__(self, expression:Expression):
        super().__init__()
        self.type = 'index'
        self.expressions.append(expression)
    
class Pipe(Operator):
    def __init__(self):
        super().__init__()
        self.type = 'pipe'

class Where(Operator):
    def __init__(self):
        super().__init__()
        self.type = 'where'
        self.parameters = []    
from Operator import Operator
import json

class Query():
    def __init__(self):
        self.statements = []

    def to_dict(self):
        return {
            "statements": [x.to_dict() for x in self.statements]
        }

    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)

class Statement():
    def __init__(self, name:str=""):
        # if empty it's the prime statement
        self.name = name
        self.operations = []
    
    def to_dict(self):
        return {
            'name': self.name,
            'operations': [x.to_dict() for x in self.operations]
        }
    
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
    
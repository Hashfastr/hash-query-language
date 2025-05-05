import json

class Function():
    def __init__(self, args:list):
        self.args = args
        self.name = self.__class__.__name__
        
    def to_dict(self):
        return {
            'type': 'function',
            'name': self.name,
            'args': self.args
        }
    
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self) -> str:
        return self.__str__()
        
    def eval(self):
        return {
            "results": []
        }
        
    def eval_chain(self, next:list):
        cur = self.eval()
        
        if len(next) == 1:
            return cur.exec_func(next)
        else:
            return cur.exec_func_chain(next)
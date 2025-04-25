from . import Operator

# Index in a database to grab data from, extremely simple. 
class Index(Operator):
    def __init__(self, expression:Expression):
        super().__init__()
        self.type = 'index'
        self.expressions.append(expression)
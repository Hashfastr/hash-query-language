from Operator import Operator

class Statement():
    def __init__(self, name:str=""):
        # if empty it's the prime statement
        self.name = name
        self.operations = []
        self.index = ""
        
    def add_operation(self, operator:Operator):
        self.operations.append(operator)
        
from HqlCompiler.Operators.Operator import Operator

class Database(Operator):
    def __init__(self):
        super().__init__()
        self.dbtype = self.type
        self.type = "Database"
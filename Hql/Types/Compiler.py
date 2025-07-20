from Hql.Exceptions import HqlExceptions as hqle

class CompilerType():
    def __init__(self):
        if len(type(self).__bases__):
            super().__init__()
            self.HqlType = type(self).__bases__[-1]
        else:
            self.HqlType = None

        self.name = self.__class__.__name__
    
    def hql_schema(self):
        if self.HqlType == None:
            raise hqle.CompilerException(f"{type(self).__name__} type defined without an Hql proto")
        return self.HqlType

    def __len__(self):
        return 1


from .Operator import Operator
from ..Expression import Expression

# Project my beloved
# Defines a number of fields to be kept in the output following this operator.
#
# {"test1":"val","test2":"val","test3":"val","test4":"val","test5":"val"}
# | project test1, test3, test5
# 
# Would result in
#
# {"test1":"val","test3":"val","test5":"val"}
# https://learn.microsoft.com/en-us/kusto/query/project-operator
class Project(Operator):
    def __init__(self, fields:list=[]):
        super().__init__()
        self.type = 'project'
    
    def gen_filter(self):
        pass
    
    def process(self, data):
        pass
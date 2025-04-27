from .Operator import Operator
from ..Expression import Expression
import polars as pl
import json

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
    def __init__(self):
        super().__init__()
        
    def advance(self, columns:list[pl.DataFrame]) -> list[pl.DataFrame]:
        new = []
        name = columns[0].columns[0]
        for i in columns:
            new.append(i.select(name).unnest(name))
            
        return new

    def merge(self, frames):
        columns = {}
        for i in frames:
            name = i.columns[0]
            
            if name not in columns:
                columns[name] = []
            
            columns[name].append(i)
            
        mergable = []
        for i in columns:
            if len(columns[i]) == 1:
                mergable.append(columns[i][0])
                continue

            new = pl.DataFrame({i: self.merge(self.advance(columns[i])).to_struct()})

            mergable.append(new)
            
        return pl.concat(mergable, how="horizontal")
    
    def get_element(self, data:pl.DataFrame, fields:list[str], index:int=0):
        if index == len(fields):
            return pl.DataFrame({fields[index-1]: data.to_struct()})
        
        split = fields[index]
    
        new = data.select(split)
        
        if len(fields) == 1:
            return new
        
        # print(new.to_dicts())
        
        if isinstance(new[split].dtype, pl.Struct):
            new = new.unnest(split)
        else:
            return pl.DataFrame({fields[index-1]: new.to_struct()})
            
        rec_data = self.get_element(new, fields, index + 1)
        
        if index == 0:
            return rec_data
        else:
            return pl.DataFrame({fields[index-1]: rec_data.to_struct()})
    
    def gen_fields(self):
        fields = []
        for i in self.expressions:
            if i.escaped:
                fields.append([i.name])
            else:
                fields.append(i.name.split('.'))
        return fields
        
    def execute(self, data:pl.DataFrame):
        fields = self.gen_fields()

        cols = []
        for i in fields:
            cols.append(self.get_element(data, i))
            
        new = self.merge(cols)
        
        return new
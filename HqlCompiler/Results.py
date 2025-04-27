import polars as pl
from .PolarsTools import PolarsTools as pltools

class Results():
    def __init__(self, results:list[pl.DataFrame]):
        self.dfs = results
        
    def to_dicts(self):
        dicts = []
        for i in self.dfs:
            dicts += i.to_dicts()
        return dicts
    
    def add(self, df:pl.DataFrame):
        merged = False
        
        for i in self.dfs:
            if i.collect_schema == df.collect_schema:
                pl.concat([i, df])
                merged = True
                break
        
        if not merged:
            self.dfs.append(df)
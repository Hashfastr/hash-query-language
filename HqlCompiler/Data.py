import polars as pl
from .PolarsTools import PolarsTools as pltools

class Data():
    ...

class Table():
    def __init__(self, init_df:pl.DataFrame=None, init_data:list[dict]=None):
        self.df = pl.DataFrame()
        self.schema = {}

        if init_df:
            self.df = init_df
            self.schema = pltools.gen_schema(self.df)

        if init_data:
            self.ingest(init_data)
        
    # def ingest(self, data:list[dict]):
    #     self.schema = 
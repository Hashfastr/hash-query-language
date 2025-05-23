import HqlCompiler.PolarsTools as pltools
import polars as pl

class Table():
    '''
    unnest here is if the data returned by your database contains a meta _source column
    '''
    def __init__(self, name:str="Table"):
        self.name = name
        self.data = None
        self.schema = None
        
    def __len__(self):
        return len(self.data)

    def gen_schema(self, data:dict):
        schema = {}
        for i in data:
            itype = type(data[i])
            
            if itype == dict:
                schema[i] = self.gen_schema(data[i])
            elif itype == list:
                schema[i] = [type(data[i][0])]
            else:
                schema[i] = itype
            
        return schema
    
    '''
    Attempts to add data to itself, if the data is not in its schema,
    then it'll do it's best to resolve.
    
    All data that could not be ingested is returned as a list.
    '''
    def add_data(self, data:list[dict], unnest:str=''):
        if not data or len(data) == 0:
            return []
        
        if not self.schema:
            if unnest == '':
                self.schema = self.gen_schema(data[0])
            else:
                self.schema = self.gen_schema(data[0][unnest])
        
        # This is to initialize the dataset
        if not self.data:
            if unnest == '':
                df = pl.from_dicts([data[0]], schema=self.schema)
            else:
                df = pl.from_dicts([data[0][unnest]], schema=self.schema)
        
        self.data = df
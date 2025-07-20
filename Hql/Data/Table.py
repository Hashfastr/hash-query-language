import polars as pl
from .Schema import Schema
from .Series import Series
from ..Exceptions import *
from ..PolarsTools import pltools
from ..Types.Compiler import CompilerType
from ..Types.Hql import HqlTypes as hqlt
import logging
from typing import Union

'''
Table for a structure of data, includes schema definition.
Mimics a pl.DataFrame
'''
class Table():
    def __init__(
            self,
            df:pl.DataFrame=None,
            series:Series=None,
            init_data:list[dict]=None,
            schema:Schema=None,
            name:str=None
        ):
        
        if hasattr(df, 'is_empty'):
            self.df = df
        else:
            self.df = pl.DataFrame()
            
        if isinstance(schema, dict):
            schema = Schema(schema=schema)
        
        self.name = name if name else ''
        self.agg = None
        self.agg_paths = None
        self.agg_schema = None
        self.series = None
        self.schema = None

        if series:
            self.series = series

        elif init_data and not schema:
            self.schema = Schema(init_data)
            init_data = self.schema.adjust_mv(init_data)
            schema = self.schema.gen_pl_schema()
            self.df = pl.from_dicts(init_data, schema=schema)
        
        elif init_data and schema:
            self.schema = schema
            self.df = pl.from_dicts(init_data, schema=schema.to_pl_schema())
        
        elif not self.df.is_empty() and schema:
            self.schema = schema
            self.df = schema.apply(self.df)

        elif not self.df.is_empty() and not schema:
            self.schema = Schema(data=self.df)

        elif schema:
            logging.warning('Schema defined in table without data')
            self.schema = schema

        else:
            self.schema = Schema()

    def __len__(self):
        if hasattr(self.df, '__len__'):
            return len(self.df)
        return 0

    def to_dicts(self):
        human = self.schema.present_complex(self.df)
        return human.to_dicts()

    def get_schema(self):
        return self.schema.schema

    def set_schema(self, schema:Schema):
        self.df = schema.apply(self.df)
        self.schema = schema

    def drop(self, path:list[str], df:pl.DataFrame=None, idx:int=0):
        if idx == 0:
            self.schema.drop(path)
            df = self.df
        
        new = {}
        for col in df:
            if col.name == path[idx]:
                if idx == len(path) - 1:
                    # silent drop
                    continue
                
                if col.dtype == pl.Struct:
                    rec = self.drop(path, df=pl.DataFrame(col).unnest(col.name), idx=idx+1)
                    if not rec.is_empty():
                        new[col.name] = rec
                
            # Not dropping
            else:
                new[col.name] = col
        
        # end of recursion
        if idx == 0:
            self.df = pl.DataFrame(new)
            return self
            
        return pl.DataFrame(new)
    
    def drop_many(self, paths:list[list[str]]):
        for path in paths:
            self.drop(path)
        return self
        
    '''
    Truncates the dataset to a given amount
    '''
    def truncate(self, amount:int):
        self.df = self.df[:amount]

    '''
    Runs a polars filter on the table
    '''
    def filter(self, expr:pl.Expr):
        try:
            self.df = self.df.filter(expr)
        except pl.exceptions.ColumnNotFoundError as e:
            raise QueryException(e.args[0])
        
    def get_value(self, path:list[str]):
        return pltools.get_element_value(self.df, path)

    @staticmethod
    def merge(tables:list["Table"]):
        max_cols = 100
        
        if not tables:
            return Table()
        
        # Quick short circuit
        if len(tables) == 1:
            return tables[0]
        
        name = tables[0].name
        
        schemas = []
        for table in tables:
            schemas.append(table.schema)
        schema = Schema.merge(schemas).schema
        
        # generate col groups
        col_groups = dict()
        for table in tables:
            # skip empty dataframes
            if isinstance(table.df, type(None)) or table.df.is_empty():
                continue

            for col in table.df:
                if col.name not in col_groups:
                    col_groups[col.name] = []
                    
                col_groups[col.name].append(col)

        new = dict()
        for key in col_groups:
            for col in col_groups[key]:
                if key not in new:
                    new[key] = col
                    continue
                
                # Canon conflict
                if new[key].dtype == pl.Struct and col.dtype == pl.Struct:
                    l = Table(df=new[key].struct.unnest(), name=name)
                    r = Table(df=col.struct.unnest(), name=name)
                    
                    new[key] = Table.merge([l, r]).df.to_struct()
                    continue
                
                for i in range(max_cols):
                    name = f'{key}_{i}'
                    
                    if name not in new:
                        new[name] = col
                        break
                    
                    if i == max_cols - 1:
                        logging.critical(f'Attempting to create more duplicate columns than allowed: {max_cols}')
                        logging.critical(f'Applicable field: {key}')
                        raise QueryException(f'Attempting to create more duplicate columns than allowed: {max_cols}') 
                
        df = pl.DataFrame(new)
        schema = Schema(schema=schema)
                
        return Table(df=df, schema=schema, name=name)
    
    @staticmethod
    def concat(tables:list["Table"]):
        df = pl.concat([x.df for x in tables])
        schema = tables[0].schema
        name = tables[0].name

        return Table(df=df, schema=schema, name=name)

    '''
    Takes in a list of path parts
    client.ip.src
    ['client', 'ip', 'src']
    Returns a Table with just the data of that path
    If not found then it returns an empty table with the parent name.
    '''
    def select(self, field:list[str]):
        if not self.assert_field(field):
            return Table(name=self.name)
        
        df = pltools.get_element(self.df, field)
        schema = self.schema.select(field)

        return Table(df=df, schema=schema, name=self.name)

    def unnest(self, field:list[str]):
        if not self.assert_field(field):
            raise QueryException(f"Could not unnest field {'.'.join(field)} from table {self.name}")
        
        df = self.get_value(field)
        
        if isinstance(df, pl.Series):
            return Series(df, self.schema.unnest(field))            
            
        else:
            schema = Schema(schema=self.schema.unnest(field))
            return Table(df=df, schema=schema, name=self.name)

    '''
    Returns the deep stripped value of a DataFrame with a single value.
    So {'destination': {'ip': hqlt.ip4}} would just return hqlt.ip4.
    A more complex case is:

    {
        'destination': {
            'ip': hqlt.ip4,
            'port': hqlt.short
        }
    }

    Which would just return:

    {
        'ip': hqlt.ip4,
        'port': hqlt.short
    }

    The idea here is if you want to extract the value of a function, this does it.
    '''
    def strip(self):
        cur = self.df
        path = []
        while isinstance(cur, pl.DataFrame) and len(cur.columns) == 1:
            key = cur.columns[0]
            cur = pltools.get_element_value(cur, [key])
            path.append(key)
        
        # Using this instead of strip to ensure we're sync
        schema = self.schema.unnest(path)
            
        return Table(df=cur, schema=schema, name=self.name)

    def rename(self, src:list[str], dest:list[str]):
        if not self.assert_field(src):
            raise QueryException('Attempting to rename a non-existing field')
        
        if self.assert_field(dest):
            raise QueryException('Attempting to rename field into an existing field')
        
        value = self.pop(src).unnest(src)
        if value.series:
            schema = value.series.type
            value = value.series.series
        else:
            schema = value.schema.schema
            value = value.df
        
        self.insert(dest, value, schema)
    
    # Inserts a piece of data at a given name
    def insert(
            self,
            name:list[str],
            value:Union[pl.DataFrame, pl.Series],
            vtype:Union[CompilerType, dict],
            cur_df:pl.DataFrame=None,
            idx:int=0
        ):
        if not hasattr(cur_df, 'is_null'):
            cur_df = self.df
            
        split = name[idx]
                
        # Endpoint
        if idx == len(name) - 1:
            # Find a unique name
            if split in cur_df:
                i = 0
                while f'{split}_{i}' in cur_df:
                    i += 1
                split = f'{split}_{i}'
                name[idx] = split
                        
            self.schema.set(name, vtype)
            new = pl.DataFrame({name[-1]: value})
        
        # Not the end, but we're now free to do whatever we want
        elif split not in cur_df:
            recurse = self.insert(name, value, vtype, cur_df=pl.DataFrame(), idx=idx + 1)
            new = pl.DataFrame({split: recurse.to_struct()})
        
        # Recurse up a nested object
        elif cur_df[split].dtype == pl.Struct:        
            recurse = self.insert(name, value, vtype, cur_df=cur_df.select(split).unnest(split), idx=idx + 1)
            cur_df = cur_df.remove(split)
            new = pl.DataFrame({split: recurse})
        
        # Conflict, a base type is where we're trying to put a struct
        else:
            i = 0
            while f'{split}_{i}' in cur_df:
                # Merging case
                if cur_df[f'{split}_{i}'].dtype == pl.Struct:
                    break
                i += 1
            split = f'{split}_{i}'
            name[idx] = split
         
            if cur_df[split].dtype == pl.Struct:
                recurse = self.insert(name, value, vtype, cur_df=cur_df.select(split).unnest(split), idx=idx + 1)
            else:
                recurse = self.insert(name, value, vtype, cur_df=pl.DataFrame(), idx=idx + 1)
            
            new = pl.DataFrame({split: recurse})
        
        new = pl.concat([new, cur_df], how='horizontal')
        
        if idx == 0:
            self.df = new
        
        return new

    def remove(self, name:list[str], cur_df:pl.DataFrame=None, idx:int=0):
        if not hasattr(cur_df, 'is_null'):
            cur_df = self.df
            
        if idx == 0 and not self.assert_field(name):
            return cur_df
            
        split = name[idx]
        mask = cur_df.remove(split)
        
        if idx == len(name) - 1:
            return mask
        
        if cur_df[split].dtype == pl.Struct:
            recurse = self.remove(name, cur_df=cur_df.unnest(split), idx=idx + 1)
            
            if not recurse.is_empty():
                recurse = pl.DataFrame({split: recurse})
                merged = pl.concat([mask, recurse], how='horizontal')
            else:
                merged = mask
        else:
            merged = mask

        return merged
            
    def pop(self, name:list[str]):
        if not self.assert_field(name):
            raise QueryException('Attempting to pop a non-existing field')
        
        # Schema is tracked through the select
        value = self.select(name)
        self.schema.pop(name)
        self.remove(name)
        
        return value
    
    # Asserts by checking against schema
    # Schema should always be sync'd with the table data
    def assert_field(self, field:list[str]):
        return self.schema.assert_field(field)
    
    def cast_in_place(self, path:list[str], cast_type:hqlt.HqlType):
        if not self.assert_field(path):
            return None
        
        self.schema.set(path, cast_type)
        self.df = self.schema.apply(self.df)

        return self
    
    def join(self, right:"Table", on:str, kind:str):
        schema = self.schema.join(right.schema, on, kind)

        if kind == 'inner':
            df = self.df.join(right.df, on=on, how='inner')
        
        elif kind == 'leftsemi':
            df = self.df.join(right.df, on=on, how='semi')

        elif kind == 'rightsemi':
            df = right.df.join(self.df, on=on, how='semi')

        elif kind == 'leftouter':
            df = self.df.join(right.df, on=on, how='left')

        elif kind == 'rightouter':
            df = right.df.join(self.df, on=on, how='left')

        elif kind == 'fullouter':
            df = self.df.join(right.df, on=on, how='full')

        elif kind == 'leftanti':
            df = self.df.join(right.df, on=on, how='anti')

        elif kind == 'rightanti':
            df = right.df.join(right.df, on=on, how='anti')

        elif kind == 'innerunique':
            left = self.df.unique(subset=[on])
            df = left.join(right.df, on=on, how='inner')

        else:
            raise QueryException(f'Invalid join kind {kind} used')
        
        return Table(df=df, schema=schema, name=self.name)

    '''
    Sorts by expression, if they exist
    '''
    def sort(self, exprs:list[pl.Expr], orders:list[bool]=None, nulls:list[bool]=None):
        orders = [True for x in exprs] if orders is None else orders
        nulls = [x for x in orders] if nulls is None else nulls
        exprs = exprs if isinstance(exprs, list) else [exprs]
        
        if len(orders) < len(exprs):
            logging.warning('Passing incomplete list of orders to table sort, defaulting to desc for missing values')
            for i in range(len(exprs) - len(orders)):
                orders.append(True)
                
        if len(nulls) < len(exprs):
            logging.warning('Passing incomplete list of nulls to table sort, defaulting to last for missing values')
            for i in range(len(exprs) - len(nulls)):
                nulls.append(True)
        
        texprs = []
        torders = []
        tnulls = []
        for idx, expr in enumerate(exprs):
            try:
                self.df.select(expr)
                texprs.append(exprs[idx])
                torders.append(orders[idx])
                tnulls.append(nulls[idx])
            except:
                continue

        # No applicable sort
        if not len(texprs):
            return self
        
        self.df = self.df.sort(by=texprs, descending=torders, nulls_last=tnulls)
        return self

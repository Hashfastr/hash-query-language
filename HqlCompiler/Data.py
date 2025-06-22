import polars as pl
from HqlCompiler.PolarsTools import pltools
from HqlCompiler.Exceptions import *

from HqlCompiler.Types.Compiler import CompilerType
from HqlCompiler.Types.Hql import HqlTypes as hqlt
from HqlCompiler.Types.Python import PythonTypes as pyt
from HqlCompiler.Types.Polars import PolarsTypes as plt

from typing import Union
import logging
import json

class Data():
    ...

class Series():
    ...

class Table():
    ...

class Schema():
    ...

class Data():
    # tables is a unique list of tables by name
    # tables_list is a non-unique list of tables.
    def __init__(self, tables:dict[Table]=None, tables_list:list[Table]=None):
        self.tables = dict()

        # empty base case
        if not tables and not tables_list:
            return

        table_groups = dict()

        if not tables_list:
            tables_list = []

        # convert everything to a list for processing
        if tables:
            for key in tables:
                tables_list.append(tables[key])

        for table in tables_list:
            if not isinstance(table, Table):
                raise CompilerException('Non-table passed to Data as init data')

        # Give names to names-less tables
        for idx, i in enumerate(tables_list):
            if i.name == None:
                i.name = f'Table {idx}'

        # Form table groups for merging
        for i in tables_list:
            if i.name not in table_groups:
                table_groups[i.name] = [i]
            else:
                table_groups[i.name].append(i)

        # Merge table groups
        for name in table_groups:
            self.tables[name] = Table.merge(tables=table_groups[name])
            
    def __len__(self):
        length = 0
        for table in self:
            length += len(table)
            
        return length

    def __iter__(self):
        tables = []
        for name in self.tables:
            tables.append(self.tables[name])
            
        return iter(tables)

    '''
    Gets tables relevant to a given table pattern
    
    * 
    gets all tables
    
    so-beats-*
    gets all tables starting with so-beats-
    
    so-network-2022.10
    Just gets the table named so-network-2022.10
    '''
    def get_tables(self, name:str):
        if '*' not in name:
            table = self.tables.get(name, None)
            
            if not table:
                raise QueryException(f'Unknown table {name} referenced')
            
            return [table]
        
        prefix = name.split('*')[0]
        
        tables = []
        for table in self:
            if table.name.startswith(prefix):
                tables.append(table)
                
        return tables
    
    def table_by_index(self, idx:int):
        key = list(self.tables.keys())[idx]
        return self.tables[key]
    
    def add_table(self, table:Table):
        if table.name in self.tables:
            raise QueryException(f'Table {table.name} already exists')
        
        self.tables[table.name] = table
        
    def replace_table(self, table:Table):
        self.tables[table.name] = table
        
    def get_schema(self):
        schemata = {}
        for table in self:
            schemata[table.name] = table.get_schema()
        
        return schemata

    # Given a path, select just the data at that path
    def select(self, path:list[str]):
        tables = []
        for table in self:
            tables.append(table.select(path))

        return Data(tables_list=tables)
    
    def unnest(self, field:list[str]):
        tables = []
        for table in self:
            new = table.unnest(field)
            
            if isinstance(new, Series):
                new = Table(series=new, name=table.name)
            
            tables.append(new)
        
        return Data(tables_list=tables)

    def to_dict(self):
        dataset = dict()
        
        dataset['data'] = {}
        for table in self:
            dataset['data'][table.name] = table.to_dicts()
            
        dataset['schema'] = self.get_schema()

        return dataset
    
    def merge(data:list[Data]):
        if len(data) == 1:
            return data[0]
        
        tables = []
        for datum in data:
            for table in datum:
                tables.append(table)

        return Data(tables_list=tables)

    # Ensures that the field exists in at least one table
    # Returns the tables where it does exists
    def assert_field(self, field:list[str]):
        exists = []
        
        if not self.tables:
            return exists
        
        for table in self:
            if table.assert_field(field):
                exists.append(table)

        if not len(exists):
            logging.warning(f"Could not find {'.'.join(field)} in any tables in the dataset")
            logging.warning(', '.join([x.name for x in self]))
        
        return exists
    
    def cast_in_place(self, field:list[str], cast_type:hqlt.HqlType):
        tables = self.assert_field(field)
        if not tables:
            return False

        for i in tables:
            i.cast_in_place(field, cast_type)

        return self

    def join(self, right:Data, on:str, kind:str='innerunique'):
        tables = []
        for lt in self:
            new = []
            for rt in right:
                new.append(lt.join(rt, on, kind))

            tables.append(Table.concat(new))
        
        return Data(tables_list=tables)
    
    def strip(self):
        new = []
        for table in self:
            new.append(table.strip())
        return Data(tables_list=new)

    def drop_many(self, paths:list[list[str]]):
        cur = self
        for path in paths:
            cur = cur.drop(path)
        return cur

    def drop(self, path:list[str]):
        new = []
        for table in self:
            new.append(table.drop(path))
        return Data(tables_list=new)
        
'''
Series for individual values, mimics a pl.Series
'''
class Series():
    def __init__(self, series:pl.Series, stype:hqlt.HqlType):
        self.series = series
        self.type = stype

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

    def merge(tables:list[Table]):
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
    
    def concat(tables:list[Table]):
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
    
    # Inserts a peice of data at a given name
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
    
    def join(self, right:Table, on:str, kind:str):
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

class Schema():
    def __init__(
            self,
            data: Union[pl.DataFrame, dict, list[dict]]=None,
            schema:dict=None,
            sample_size:int=1
        ):
        
        self.schema = dict()

        if schema:
            if isinstance(schema, Schema):
                self.schema = schema.schema
            else:
                self.schema = schema
            
            self.schema = Schema.normalize(self.schema)
        elif isinstance(data, list):
            sample = data[:sample_size] if sample_size > 0 else data
            self.schema = Schema.from_json(sample)
        elif isinstance(data, dict):
            self.schema = Schema.from_json([data])
        elif isinstance(data, pl.DataFrame):
            self.schema = Schema.from_df(data)
        elif data:
            raise CompilerException(f'Non-supported type passed to Schema init {type(data)}')
        
        # Pass through empty case else we get an hqlt.object([])
        if isinstance(self.schema, dict) and len(self.schema):
            self.schema = self.convert_schema(target='hql')
    
    def __len__(self):
        if hasattr(self.schema, 'len'):
            return len(self.schema)
        
        elif self.schema != None:
            return 1
        
        else:
            return 0
    
    def merge(schemata:list):
        if len(schemata) == 1:
            return schemata[0]
        
        max_cols = 100
        
        # Gen keygroups
        keygroups = dict()
        for schema in schemata:
            if isinstance(schema, Schema):
                schema = schema.schema
            
            for key in schema:
                if key not in keygroups:
                    keygroups[key] = [schema[key]]
                else:
                    keygroups[key].append(schema[key])

        new = dict()
        for key in keygroups:
            for schema in keygroups[key]:
                if key not in new:
                    new[key] = schema
                    continue
            
                # Canon conflict
                if isinstance(new[key], dict) and isinstance(schema, dict):
                    new[key] = Schema.merge([new[key], schema]).schema
                    continue
                
                # Find a free name
                for j in range(max_cols):
                    name = f'{key}_{j}'
                    
                    # This is the case that all previous cols were conflicting
                    if name not in new:
                        new[name] = schema
                        break
                    
                    if j == max_cols - 1:
                        logging.critical(f'Attempting to create more duplicate columns than allowed: {max_cols}')
                        logging.critical(f'Applicable field: {key}')
                        raise QueryException(f'Attempting to create more duplicate columns than allowed: {max_cols}')

        return Schema(schema=new)

    '''
    Created to solve the problem of nested Schema objects in a schema dict.
    Just unnests them such that we have a pure dict structure.
    '''
    def normalize(node):
        if isinstance(node, Schema):
            node = node.schema
        
        if isinstance(node, dict):
            new = dict()
            for key in node:
                new[key] = Schema.normalize(node[key])
            return new
        
        else:
            return node

    # Extract the schema for a given set of fields
    def select(self, field:list[str]):
        cur = self.unnest(field)
        for part in field[::-1]:
            cur = {part: cur}
        return Schema(schema=cur)

    def select_many(self, fields:list[list[str]]):
        schemas = []
        for field in fields:
            schemas.append(self.select(field))
        return Schema.merge(schemas)
    
    def unnest(self, field:list[str]):
        cur = self.schema
        for part in field:
            if part not in cur:
                return None
            else:
                cur = cur[part]
                
        return Schema(schema=cur)
    
    def copy(self):
        from copy import deepcopy
        return Schema(schema=deepcopy(self.schema))
        
    '''
    Like unnest but returns an appropriate hqlt.object on a dict reference
    '''
    def get_type(self, field:list[str]):
        dtype = self.unnest(field)
       
        #if isinstance(dtype, dict):
        #    dtype = hqlt.object(list(dtype.keys()))
           
        return dtype

    '''
    Returns the deep stripped value of a dict with a single value.
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

    Doesn't return a schema object as it might be a type or a dict
    Typically this is called with a named expression, so it's gonna build the schema anyways.
    '''
    def strip(self):
        cur = self.schema
        while isinstance(cur, dict) and len(cur) == 1:
            key = list(cur.keys())[0]
            cur = cur[key]
        return cur
    
    def rename(self, src:list[str], dest:list[str]):
        if not self.assert_field(src):
            raise QueryException('Attempting to rename a non-existing field')
        
        if self.assert_field(dest):
            raise QueryException('Attempting to rename field into an existing field')
        
        src_type = self.pop(src)
        
        cur = self.schema
        for idx, i in enumerate(dest):
            if idx == len(dest) - 1:
                cur[i] = src_type
            else:
                cur = cur[i]
                
    def pop(self, name:list[str]):
        if not self.assert_field(name):
            raise QueryException('Attempting to pop a non-existing field')
        
        cur = self.schema
        for idx, i in enumerate(name):
            if idx == len(name) - 1:
                src_type = cur.pop(i)
            else:
                cur = cur[i]
                
        return src_type

    def drop(self, path:list[str], schema:dict=None, idx:int=0):
        if idx == 0:
            schema = self.schema
        
        new = {}
        for key in schema:
            if key == path[idx]:
                if idx == len(path) - 1:
                    # Silent drop
                    continue
                
                if isinstance(schema[key], dict):
                    rec = self.drop(path, schema=schema[key], idx=idx+1)
                    if rec:
                        new[key] = rec
            
            # Don't have to do anything
            else:
                new[key] = schema[key]
                
        if idx == 0:
            self.schema = new
            return self
            
        return new
    
    def drop_many(self, paths:list[list[str]]):
        for path in paths:
            self.drop(path)
        return self
    
    '''
    Set a field to a specific type in the schema
    apply is then expected to be ran
    '''
    def set(self, path:list[str], htype:Union[hqlt.HqlType, Schema, dict], schema:Union[dict, Schema]=None, idx:int=0):
        if isinstance(htype, Schema):
            htype = htype.schema
        
        schema = schema if schema != None else self.schema
        if isinstance(schema, Schema):
            schema = schema.schema

        split = path[idx]

        if idx == len(path) - 1:
            schema[split] = htype
            return schema

        if split in schema:
            schema[split] = self.set(path, htype, schema=schema[split], idx=idx+1)
        else:
            schema[split] = self.set(path, htype, {}, idx=idx+1)

        if idx == 0:
            self.schema = schema
        else:
            return schema

    '''
    Generates a schema with types replaced with their polars primatives
    schema parameter required for recursion
    '''
    def convert_schema(self, schema:Union[dict, type]=None, target:str='hql'):
        supported = ('hql', 'polars')
        
        if target not in supported:
            logging.critical(f'Unsupported schema conversion type {target}')
            logging.critical(f'Supported schemas: {supported}')
            raise CompilerException(f'Unsupported schema conversion type {target}')
        
        if not schema:
            schema = self.schema
        
        # Endpoint in the tree
        # Expected to be a type we can convert
        if not isinstance(schema, dict):
            if hasattr(schema, 'hql_schema') and target == 'hql':
                return schema.hql_schema()
            
            if hasattr(schema, 'pl_schema') and target == 'pl':
                return schema.pl_schema()
            
            raise CompilerException(f'Unsupported type to convert {schema}')

        # Base case, create empty object/struct
        if len(schema) == 0:            
            if target == 'hql':
                return hqlt.object([])
            elif target == 'polars':
                return plt.Struct([])

        # Recurse on a populated dict
        target_schema = dict()
        for key in schema:
            target_schema[key] = self.convert_schema(schema=schema[key], target=target)
        
        return target_schema

    def gen_pl_list_schema(self, schema:Union[dict, list, hqlt.HqlType]):
        if isinstance(schema, dict):
            return self.gen_pl_schema(schema)
        
        elif isinstance(schema, list):
            return [self.gen_pl_list_schema(schema[0])]
        
        else:
            return schema.pl_schema()
        
    '''
    Generates a schema for use in polars using their types
    Uses structs for nested objects instead of json objects
    '''
    def gen_pl_schema(self, schema:dict=None):
        schema = schema if schema else self.schema
        
        if not isinstance(schema, dict):
            return schema.pl_schema()
        
        new_schema = {}
        for key in schema:
            if isinstance(schema[key], dict):
                if len(schema[key]):
                    new_schema[key] = pl.Struct(self.gen_pl_schema(schema=schema[key]))
                else:
                    new_schema[key] = pl.Struct([])

            elif isinstance(schema[key], list):
                new_schema[key] = self.gen_pl_list_schema(schema[key])
                
            else:
                new_schema[key] = schema[key].pl_schema()
    
        return new_schema

    '''
    Gen schema from dicts
    Uses python typing
    '''
    def from_json(data:list[dict]):
        # get a set of keys to handle
        keyset = set()
        for row in data:
            if row:
                keyset |= set(row.keys())
        keyset = list(keyset)
        
        # if we have no keys then we have an empty dict
        if not len(keyset):
            return pyt.dict([])

        new = dict()
        for key in keyset:
            typeset = set()
            for row in data:
                if key not in row:
                    continue
                    
                if isinstance(row[key], dict):
                    typeset.add(dict)
                
                elif isinstance(row[key], list):
                    typeset.add(pyt.list(pyt.resolve_mv(row[key])))
                    
                else:
                    typeset.add(pyt.from_name(type(row[key]).__name__)())
            
            typeset = list(typeset)

            # recurse on an object
            if dict in typeset:
                # The only two acceptable existences of dict being in a typeset
                # are {dict} and {dict, pyt.null}
                if len(typeset) != 1 and pyt.NoneType not in typeset:
                    raise Exception(f"Cannot merge types {list(typeset)}")
                
                # Unnest the nested dict
                sub_data = []
                for row in data:
                    if key in row:
                        sub_data.append(row[key])

                # Create the new schema from the unnested dict
                new[key] = Schema(data=sub_data).schema

            else:
                # Find the best type
                new[key] = pyt.resolve_conflict(typeset)
                
        return new
    
    '''
    Generates a schema using polars typing
    '''
    def from_df(df:pl.DataFrame) -> dict:
        schema = dict()
        
        for col in df:
            if isinstance(col.dtype, pl.Struct):
                schema[col.name] = Schema.from_df(pl.DataFrame(col).unnest(col.name))
                continue
            
            if col.dtype == pl.Object:
                raise Exception('poop')

            schema[col.name] = plt.from_pure_polars(col.dtype)
            
        return schema

    # Adjusts json to multivalue
    def adjust_mv(self, data:list[dict], schema:dict=None) -> list[dict]:
        schema = schema if schema != None else self.schema
        
        # Loop through each defined multivalue field
        for key in schema:
            if isinstance(schema[key], dict):
                rows = []
                for row in data:
                    if key in row:
                        rows.append(row[key])
                        
                self.adjust_mv(data, schema=schema[key])
            
            if not isinstance(schema[key], hqlt.multivalue):
                continue
            
            for row in data:
                if key in row and not isinstance(row[key], list):
                    row[key] = [row[key]]

        return data
    
    '''
    Applies a schema to a dataset
    If a col is not defined in the schema, then it just skips over it
    Errors if a col defined in the schema is not in the df
    '''
    def apply(self, df:pl.DataFrame, schema:dict=None):
        if isinstance(schema, Schema):
            schema = schema.schema
        
        if schema == None:
            schema = self.schema
        
        # Single value schema    
        if not isinstance(schema, dict):
            return schema.cast(df)
        
        # Check the schema doesn't map to missing cols
        for key in schema:
            if key not in df:
                logging.warning(f"{key} not found in dataframe {', '.join(df.columns)}")
                raise CompilerException('Attempting to apply a schema to a mismatched dataframe!')
        
        new = {}
        for col in df:
            key = col.name
            
            # Handle undefined types, don't have to worry about them, carry on.
            if key not in schema:
                new[key] = col
                continue
            
            if isinstance(schema[key], dict):
                new[key] = self.apply(pl.DataFrame(col).unnest(key), schema[key]).to_struct()
                continue
            
            new[key] = schema[key].cast(col)
            
        return pl.DataFrame(new)
    
    # Asserts by attempting to retrieve the field's value
    def assert_field(self, field:list[str]):
        if self.unnest(field) == None:
            return False
        else:
            return True
        
    def present_complex(self, df:pl.DataFrame, schema:dict=None):
        schema = schema if schema != None else self.schema

        newdf = {}
        for col in df:
            if col.name not in schema:
                newdf[col.name] = col
                continue
            
            if isinstance(schema[col.name], dict):
                newdf[col.name] = self.present_complex(col.struct.unnest(), schema[col.name]).to_struct()
                continue

            if schema[col.name].complex:
                newdf[col.name] = schema[col.name].human(col)
            else:
                newdf[col.name] = col

        return pl.DataFrame(newdf)

    def join(self, right:Schema, on:str, kind:str):
        import copy
        
        # all of these are semantically the same schema wise
        if kind in ('inner', 'leftsemi', 'rightsemi', 'innerunique', 'leftouter', 'rightouter', 'fullouter'):
            new = copy.deepcopy(self.schema)
            for i in right.schema:
                if i in new and i != on:
                    new[f'{i}_right'] = new[i]
            
            return Schema(schema=new)

        elif kind == 'leftanti':
            return self

        elif kind == 'rightanti':
            return right

        else:
            raise QueryException(f'Invalid join kind {kind} used')
            

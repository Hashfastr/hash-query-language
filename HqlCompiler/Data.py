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
            # no need to merge, unique table
            if len(table_groups[name]) == 1:
                self.tables[name] = table_groups[name][0]
                continue
            
            self.tables[name] = Table.merge(tables=table_groups[name])
            
    def __len__(self):
        length = 0
        for i in self.tables:
            length += len(self.tables[i])
            
        return length

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
        for table in self.tables:
            if table.startswith(prefix):
                tables.append(self.tables[table])
                
        return tables
    
    def add_table(self, table:Table):
        if table.name in self.tables:
            raise QueryException(f'Table {table.name} already exists')
        
        self.tables[table.name] = table
        
    def replace_table(self, table:Table):
        self.tables[table.name] = table
        
    def get_schema(self):
        schemata = {}
        for name in self.tables:
            schemata[name] = self.tables[name].get_schema()
        
        return schemata

    # Given a list of string paths, get a dataset containing only those fields
    def select(self, fields:list[str]):
        tables = []
        for i in self.tables:
            tables.append(self.tables[i].select(fields))

        return Data(tables_list=tables)
    
    def unnest(self, field:list[str]):
        tables = []
        for i in self.tables:
            new = self.tables[i].unnest(field)
            print(type(new))
            tables.append(new)
        
        return Data(tables_list=tables)

    def to_dict(self):
        dataset = dict()
        
        dataset['data'] = {}
        for i in self.tables:
            dataset['data'][i] = self.tables[i].to_dicts()
            
        dataset['schema'] = {}
        for i in self.tables:
            dataset['schema'][i] = self.tables[i].get_schema()

        return dataset
    
    def merge(data:list[Data]):
        tables = []
        for datum in data:
            for name in datum.tables:
                tables.append(datum.tables[name])

        return Data(tables_list=tables)

    # Ensures that the field exists in at least one table
    # Returns the tables where it does exists
    def assert_field(self, field:list[str]):
        exists = []
        for i in self.tables:
            if self.tables[i].assert_field(field):
                exists.append(self.tables[i])

        if not len(exists):
            logging.warning(f"Invalid field {'.'.join(field)} in table {i}")
        
        return exists
    
    def cast_in_place(self, field:list[str], cast_type:hqlt.HqlType):
        tables = self.assert_field(field)
        if not tables:
            return False

        for i in tables:
            i.cast_in_place(field, cast_type)

        return self

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
        
        self.name = name
        self.df = None
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
        
        elif not df.is_empty() and schema:
            self.schema = schema
            self.df = schema.apply(df)

        elif not df.is_empty() and not schema:
            self.df = df
            self.schema = Schema(data=df)

        elif schema:
            self.schema = schema

    def __len__(self):
        return len(self.df)

    def to_dicts(self):
        return self.df.to_dicts()

    def get_schema(self):
        return self.schema.schema

    def set_schema(self, schema:Schema):
        self.df = schema.apply(self.df)
        self.schema = schema
        
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
        return pltools.get_element_value(self.df, fields=path)

    def merge(tables:list[Table]=None, schema:Schema=None):
        if not tables:
            return Table()
        
        name = tables[0].name
        
        # gen schema
        if not schema:
            schemas = []
            for table in tables:
                schemas.append(table.schema)
                
            schema = Schema.merge(schemas)
        
        # generate col groups
        col_groups = {}
        for table in tables:
            # skip empty dataframes
            if isinstance(table.df, type(None)) or table.df.is_empty():
                continue
            
            for col in table.df:
                if col.name not in col_groups:
                    col_groups[col.name] = []
                    
                col_groups[col.name].append(col)
        
        cols = {}
        for col in col_groups:
            if len(col_groups[col]) == 1:
                cols[col] = col_groups[col][0]
                continue
            
            if isinstance(schema[col], dict):
                ...
                
        # df = pltools.merge(dfs)
        
        df = pl.DataFrame(cols)
        
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
            return Series(df, self.schema.get_type(field))            
            
        else:
            schema = Schema(schema=self.schema.get_type(field))
            return Table(df=df, schema=schema, name=self.name)
            
    def assert_field(self, field:list[str]):
        return self.schema.assert_field(field)
    
    def cast_in_place(self, field:list[str], cast_type:hqlt.HqlType):
        if not self.assert_field(field):
            return None
        
        self.schema.set(field=field, htype=cast_type)
        self.df = self.schema.apply(self.df)

        return self

class Schema():
    def __init__(
            self,
            data: Union[pl.DataFrame, dict, list[dict]]=None,
            schema:dict=None,
            sample_size:int=1
        ):
        
        self.schema = dict()

        if schema:
            self.schema = schema
        elif isinstance(data, list):
            sample = data[:sample_size] if sample_size > 0 else data
            self.schema = Schema.from_json(sample)
        elif isinstance(data, dict):
            self.schema = Schema.from_json([data])
        elif isinstance(data, pl.DataFrame):
            self.schema = Schema.from_df(data)
        elif data:
            raise CompilerException(f'Non-supported type passed to Schema init {type(data)}')
        
        # Immediately convert to hql schema
        self.schema = self.convert_schema(target='hql')
                
    def merge(schemata:list):
        new = dict()
        for idx, i in enumerate(schemata):
            if isinstance(i, Schema):
                i = i.schema

            for j in i:
                if j in new:
                    key = f'{j}.{idx - 1}'
                    new[key] = new.pop(j)
                    key = f'{j}.{idx}'
                else:
                    key = j

                if isinstance(i[j], dict):
                    new[key] = Schema.merge([i[j]])

                new[key] = i[j]

        return Schema(schema=new)

    # Extract the schema for a given set of fields
    def select(self, field:list[str]):
        cur = self.unnest(field).schema
        for part in field[::-1]:
            cur = {part: cur}
        return Schema(schema=cur)
    
    def unnest(self, field:list[str]):
        cur = self.schema
        for part in field:
            if part not in cur:
                raise QueryException(f"Referenced field {'.'.join(field)} not in schema")
            cur = cur[part]
        return Schema(schema=cur)

    # Generates a schema with types replaced with their polars primatives
    # schema parameter required for recursion
    def convert_schema(self, schema:dict=None, target:str='hql'):
        supported = ('hql', 'polars')
        
        if target not in supported:
            logging.critical(f'Unsupported schema conversion type {target}')
            logging.critical(f'Supported schemas: {supported}')
            raise CompilerException(f'Unsupported schema conversion type {target}')
        
        if not schema:
            schema = self.schema
            
        if not isinstance(schema, dict):
            return schema

        # Base case, create empty object/struct
        if len(schema) == 0:
            if target == 'hql':
                return hqlt.object([])
            elif target == 'polars':
                return plt.Struct([])

        target_schema = dict()
        for key in schema:            
            element = schema[key]
            
            if element == {}:
                if target == 'hql':
                    target_schema[key] = hqlt.null()
                elif target == 'polars':
                    target_schema[key] = pl.Null()

            # Recurse case
            elif isinstance(element, dict):
                target_schema[key] = self.convert_schema(schema=element, target=target)

            else:
                if target == 'hql':
                    target_schema[key] = element.hql_schema()
                elif target == 'polars':
                    target_schema[key] = element.pl_schema()
                
        return target_schema

    '''
    Generates a schema for use in polars using their types
    Uses structs for nested objects instead of json objects
    '''
    def gen_pl_schema(self, schema:dict=None):
        schema = schema if schema else self.schema
        
        new_schema = {}
        for key in schema:
            if isinstance(schema[key], dict):
                if len(schema[key]):
                    new_schema[key] = pl.Struct(self.gen_pl_schema(schema=schema[key]))
                else:
                    new_schema[key] = pl.Struct([])
                    
                continue
            
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
                schema[col.name] = Schema.from_df(pl.DataFrame(col))
                
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
    Set a field to a specific type in the schema
    apply is then expected to be ran
    '''
    def set(self, path:list[str], htype:hqlt.HqlType):
        schema = self.schema
        
        for idx, field in enumerate(path):
            if field in schema:
                if isinstance(schema[field], dict):
                    schema = schema[field]
                    continue
                elif idx == len(path) - 1:
                    schema = htype
                    return True
            
            return False
        
        return False
    
    '''
    Applies a schema to a dataset
    '''
    def apply(self, df:pl.DataFrame, schema:dict=None):
        newdf = {}
        schema = schema if schema else self.schema
                
        if schema == None:
            return pl.DataFrame()

        for col in df:
            # Base case, we don't specify anything in the target schema
            # so pass through, and fill out the missing schema value
            if col.name not in schema:
                newdf[col.name] = col

            # Case to recurse on a nested object
            elif col.dtype == pl.Struct and not isinstance(schema[col.name], hqlt.object):
                subdata = pl.DataFrame(
                    df.select(col.name).unnest(col.name)
                )
            
                newdf[col.name] = self.apply(
                    subdata, 
                    schema=schema[col.name]
                ).to_struct()
                                
            else:
                newdf[col.name] = schema[col.name].cast(col)
             
        return pl.DataFrame(newdf)

    '''
    Gets the type of a given path in the schema
    '''
    def get_type(self, field:list[str]):
        schema = self.schema

        for idx, part in enumerate(field):
            if part in schema:
                if isinstance(schema[part], dict):
                    schema = schema[part]
                    continue
                elif idx == len(field) - 1:
                    return schema.get(part, None)
                else:
                    return None
                        
            return None
        
        return schema
    
    def assert_field(self, field:list[str]):
        if self.get_type(field) == None:
            return False
        else:
            return True
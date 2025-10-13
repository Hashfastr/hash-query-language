import logging
from typing import TYPE_CHECKING, Union

import polars as pl

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Types.Compiler import CompilerType 

if TYPE_CHECKING:
    from Hql.Types.Hql import HqlTypes as hqlt
    from Hql.Types.Compiler import CompilerType

class Schema():
    def __init__(
            self,
            data: Union[pl.DataFrame, dict, list[dict], None]=None,
            schema:Union[dict, None]=None,
            sample_size:int=1
        ):
        from Hql.Types.Compiler import CompilerType
        
        self.schema:dict = dict()

        if schema:
            normalized = self.normalize(schema)
            self.schema = normalized

        # This is in the case of sample json data
        # A list of dicts
        elif isinstance(data, list):
            sample = data[:sample_size] if sample_size > 0 else data
            self.schema = Schema.from_json(sample)

        # Instanciate from a single json object
        elif isinstance(data, dict):
            self.schema = Schema.from_json([data])

        # Instanciate from a Polars DataFrame
        elif isinstance(data, pl.DataFrame):
            self.schema = Schema.from_df(data)

        # Whoopsie
        elif data:
            raise hqle.CompilerException(f'Non-supported type passed to Schema init {type(data)}')
        
        # Pass through empty case else we get an hqlt.object([])
        # Otherwise immediately convert to HqlTypes
        if isinstance(self.schema, dict) and len(self.schema):
            self.schema = self.convert_schema(target='hql')
    
    def __len__(self) -> int:
        if hasattr(self.schema, '__len__'):
            return len(self.schema)
        
        elif self.schema != None:
            return 1
        
        else:
            return 0

    def __bool__(self) -> bool:
        if len(self.schema):
            return True
        return False

    def to_dict(self, recurse:Union[None, dict]=None) -> dict:
        schema = recurse if recurse else self.schema

        out = dict()
        for key in schema:
            if isinstance(schema[key], dict):
                out[key] = self.to_dict(recurse=schema[key])
            else:
                out[key] = schema[key].name

        return out
    
    @staticmethod
    def merge(schemata:list[Union['Schema', dict]]) -> 'Schema':
        from Hql.Types.Compiler import CompilerType

        # Gen keygroups
        keygroups = dict()
        for schema in schemata:
            schema = schema if isinstance(schema, dict) else schema.schema
            for key in schema:
                if key not in keygroups:
                    keygroups[key] = [schema[key]]
                else:
                    keygroups[key].append(schema[key])

        new = dict()
        for key in keygroups:
            new[key] = keygroups[key][0]

            if len(keygroups[key]) == 1:
                continue

            for schema in keygroups[key][1:]:
                if isinstance(schema, CompilerType):
                    if type(schema) == type(new[key]):
                        continue
                    new_key = f'{key}_{schema.name}'
                    new[new_key] = schema
                elif isinstance(new[key], CompilerType) and isinstance(schema, dict):
                    new_key = f'{key}_object'
                    if new_key not in new:
                        new[new_key] = schema
                    else:
                        new[new_key] = Schema.merge([new[new_key], schema]).schema
                else:
                    new[key] = Schema.merge([new[key], schema]).schema

        return Schema(schema=new)

    '''
    Created to solve the problem of nested Schema objects in a schema dict.
    Just unnests them such that we have a pure dict structure.
    '''
    def normalize(self, node:Union[dict, 'Schema', None]=None) -> Union[dict, 'CompilerType']:
        from Hql.Types.Compiler import CompilerType

        if node == None:
            node = self.schema

        if isinstance(node, Schema):
            node = node.schema

        if isinstance(node, CompilerType):
            return node

        new = dict()
        for key in node:
            new[key] = self.normalize(node[key])
        return new

    # Isolate the schema at a given path
    def select(self, path:list[str]) -> "Schema":
        cur = self.unnest(path).schema
        for part in path[::-1]:
            cur = {part: cur}
        return Schema(schema=cur)

    def select_many(self, fields:list[list[str]]):
        schemas = []
        for field in fields:
            schemas.append(self.select(field))
        return Schema.merge(schemas)
    
    def unnest(self, path:list[str]) -> "Schema":
        cur = self.schema
        for part in path:
            if part not in cur:
                return Schema()
            else:
                cur = cur[part]
                
        return Schema(schema=cur)
    
    def copy(self):
        from copy import deepcopy
        return Schema(schema=deepcopy(self.schema))
        
    '''
    Descriptive rename of unnest, might remove later
    '''
    def get_type(self, path:list[str]):
        return self.unnest(path)

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
    def strip(self) -> Union[dict, 'hqlt.HqlType']:
        cur = self.schema
        while isinstance(cur, dict) and len(cur) == 1:
            key = list(cur.keys())[0]
            cur = cur[key]
        return cur
    
    def rename(self, src:list[str], dest:list[str]):
        if not self.assert_field(src):
            raise hqle.QueryException('Attempting to rename a non-existing field')
        
        if self.assert_field(dest):
            raise hqle.QueryException('Attempting to rename field into an existing field')
        
        src_type = self.pop(src)
        
        cur = self.schema
        for idx, i in enumerate(dest):
            if idx == len(dest) - 1:
                cur[i] = src_type
            else:
                cur = cur[i]
                
    def pop(self, name:list[str]):
        if not self.assert_field(name):
            raise hqle.QueryException('Attempting to pop a non-existing field')
        
        src_type = hqlt.null()
        cur = self.schema
        for idx, i in enumerate(name):
            if idx == len(name) - 1:
                src_type = cur.pop(i)
            else:
                cur = cur[i]
                
        return src_type

    def drop(self, path:list[str], schema:Union[dict, None]=None, idx:int=0):
        if schema == None:
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
    Set a field to a specific type in the schema apply is then expected to be ran
    '''
    def set(self, path:list[str], htype:Union['hqlt.HqlType', "Schema", dict], schema:Union[dict, "Schema", None]=None, idx:int=0):
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
    Generates a schema converted to a given schema target.
    Default is HqlTypes
    '''
    def convert_schema(self, schema:Union[dict, type, None]=None, target:str='hql') -> dict:
        supported = ('hql', 'polars')
        
        if target not in supported:
            logging.critical(f'Unsupported schema conversion type {target}')
            logging.critical(f'Supported schemas: {supported}')
            raise hqle.CompilerException(f'Unsupported schema conversion type {target}')
        
        if not schema:
            schema = self.schema

        # Endpoint in the tree
        # Expected to be a type we can convert
        if not isinstance(schema, dict):
            if hasattr(schema, 'hql_schema') and target == 'hql':
                return schema.hql_schema()
            
            if hasattr(schema, 'pl_schema') and target == 'pl':
                return schema.pl_schema()
            
            raise hqle.CompilerException(f'Unsupported type to convert {schema}')

        # Base case, create empty object/struct
        if len(schema) == 0:            
            return {}

        # Recurse on a populated dict
        target_schema = dict()
        for key in schema:
            if not schema[key]:
                target_schema[key] = hqlt.null()
                continue
            
            target_schema[key] = self.convert_schema(schema=schema[key], target=target)
        
        return target_schema

    def gen_pl_list_schema(self, schema:Union[dict, list, 'hqlt.HqlType']):
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
    def gen_pl_schema(self, schema:Union[None, dict]=None):
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
    @staticmethod
    def from_json(data:list[dict])-> dict:
        from Hql.Types.Python import PythonTypes as pyt

        # get a set of keys to handle
        keyset = set()
        for row in data:
            if row:
                keyset |= set(row.keys())
        keyset = list(keyset)
        
        # if we have no keys then we have an empty dict
        if not len(keyset):
            return {}

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
    @staticmethod
    def from_df(df:pl.DataFrame) -> dict:
        from Hql.Types.Polars import PolarsTypes as plt

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
    def adjust_mv(self, data:list[dict], schema:Union[dict, None]=None) -> list[dict]:
        from Hql.Types.Hql import HqlTypes as hqlt

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
    def apply(self, df:Union[pl.DataFrame, pl.Series], schema:Union[None, dict, 'Schema', CompilerType]=None):
        if isinstance(schema, Schema):
            schema = schema.schema
        
        if schema == None:
            schema = self.schema
        
        # Single value schema
        if isinstance(schema, CompilerType):
            if not isinstance(df, pl.Series):
                raise hqle.CompilerException('Attempting singular type cast on a dataframe ')
            return schema.cast(df)
        
        new = {}
        
        # Had this here to handle cases where the schema defines non-existing cols
        # This is fine, would likely help the receiving program.
        # We don't operate from the schema anyways, but from the dataframe
        # Keeping as we *might* want to do something?
        for key in schema:
            if key not in df:
                # logging.warning(f"{key} not found in dataframe {', '.join(df.columns)}, manually adding")
                # new[key] = pl.Series(name=key, values=[None] * df.height)
                pass
        
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
        
    def present_complex(self, df:pl.DataFrame, schema:Union[None, dict]=None):
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

    def join(self, right:"Schema", on:str, kind:str):
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
            raise hqle.QueryException(f'Invalid join kind {kind} used')
            

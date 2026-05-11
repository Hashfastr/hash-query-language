import logging
from typing import TYPE_CHECKING, Sequence, Union, Optional

import polars as pl

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Types.Compiler import CompilerType 
from Hql.Types.Hql import SchemaDT

if TYPE_CHECKING:
    from Hql.Types.Hql import HqlTypes as hqlt
    from Hql.Types.Compiler import CompilerType
    from Hql.Expressions import Reference
    from Hql.Types.Hql import HqlTypes as hqlt

class Schema():
    def __init__(
            self,
            schema:Union[SchemaDT, 'hqlt.object', None]=None,
            data:Union[pl.DataFrame, dict, list[dict], None]=None,
            sample_size:int=1
        ):
        from Hql.Types.Hql import HqlTypes as hqlt
        
        self.schema:hqlt.object = hqlt.object(dict())

        if schema:
            self.schema = schema if isinstance(schema, hqlt.object) else hqlt.object(schema)
            self.normalize()
        
        # Pass through empty case else we get an hqlt.object([])
        # Otherwise immediately convert to HqlTypes
        if len(self.schema):
            self.convert_schema()

    # do this here if we have sample data
    def __new__(cls,
            schema:Union[SchemaDT, 'hqlt.object', None]=None,
            data:Union[pl.DataFrame, dict, list[dict], None]=None,
            sample_size:int=1
        ) -> 'Schema':
            
        if isinstance(data, (list, dict)):
            if isinstance(data, dict):
                data = [data]

            sample = data[:sample_size] if sample_size > 0 else data
            return Schema.from_json(sample)

        # Instanciate from a Polars DataFrame
        elif isinstance(data, pl.DataFrame):
            return Schema.from_df(data)
        
        return super().__new__(cls)
    
    def __len__(self) -> int:
        if hasattr(self.schema, '__len__'):
            return len(self.schema)
        else:
            return 0

    def __bool__(self) -> bool:
        return bool(self.schema)

    def __contains__(self, item:'Reference') -> bool:
        cur = self.schema
        for i in item.list():
            if not isinstance(cur, dict) or i not in cur:
                return False
            cur = cur[i]
        return True

    def __iter__(self):
        return iter(self.blowup_schema())

    def blowup_schema(self) -> list[tuple['Reference', CompilerType]]:
        from Hql.Expressions import NamedReference, Path
        
        def bs(schema:SchemaDT) -> list[tuple['Reference', CompilerType]]:
            out = []
            for key in schema:
                name = NamedReference(key)
                cur = schema[key]

                if isinstance(cur, hqlt.object):
                    cur = cur.schema

                if isinstance(cur, dict):
                    recurse = bs(cur)
                    for path, stype in recurse:
                        path = Path([name, path])
                        out.append((path, stype))
                else:
                    out.append((name, schema[key]))

            return out

        return bs(self.schema.schema)

    def to_dict(self) -> dict:
        return self.schema.to_dict()
    
    @staticmethod
    def merge(schemata:list['Schema']) -> 'Schema':
        from Hql.Types.Hql import HqlTypes as hqlt

        # generates key groups looking for conflicts
        # only does shallow level
        def gkg(schemata:list[dict]):
            keygroups = dict()
            for schema in schemata:
                for key in schema:
                    if key not in keygroups:
                        keygroups[key] = [schema[key]]
                    elif schema[key] not in keygroups[key]:
                        keygroups[key].append(schema[key])
            return keygroups

        # Create renames based on dupes
        # Shallow level only
        def rename(keygroups:dict) -> dict:
            new = dict()
            for key in keygroups:
                # recursable objects
                objs = []
                # normal singular types
                types:list[hqlt.HqlType] = []

                for i in keygroups[key]:
                    if isinstance(i, dict):
                        objs.append(i)
                    else:
                        types.append(i)

                if objs:
                    types = [hqlt.object(rename(gkg(objs)))] + types

                for i in types:
                    if key not in new:
                        new[key] = i
                    else:
                        new[f'{key}_{i.name}'] = i

            return new

        keygroups = gkg([x.schema for x in schemata])
        new = rename(keygroups)

        return Schema(schema=new)

    '''
    Created to solve the problem of nested Schema objects in a schema dict.
    Just unnests them such that we have a pure dict structure.
    '''
    def normalize(self):
        from Hql.Data import Schema
        from Hql.Types.Hql import HqlTypes as hqlt

        def n(node:Union[dict, 'Schema']) -> dict:
            if isinstance(node, Schema):
                return n(node.schema)

            new = dict()
            for key in node:
                if isinstance(node[key], (dict, Schema)):
                    new[key] = n(node[key])
                elif isinstance(node[key], hqlt.object) and node[key].schema:
                    new[key] = n(node[key].schema)
                else:
                    new[key] = node[key]
            return new

        self.schema = n(self.schema)
        return self

    # Isolate the schema at a given path
    def select(self, path:'Reference') -> "Schema":
        meat = self.unnest(path)
        cur = meat.schema if isinstance(meat, Schema) else meat
        for part in path.list()[::-1]:
            cur = {part: cur}
        # The above loop always runs even when path length is 1
        # It it always be a dict, linter is unsure of this
        assert isinstance(cur, dict)
        return Schema(schema=cur)

    def select_many(self, paths:Sequence['Reference']):
        schemas = []
        for path in paths:
            schemas.append(self.select(path))
        return Schema.merge(schemas)
    
    def unnest(self, path:'Reference') -> Union['Schema', 'hqlt.HqlType']:
        cur = self.schema
        for part in path.list():
            if not isinstance(cur, dict) or part not in cur:
                return Schema()
            else:
                cur = cur[part]
        
        if isinstance(cur, dict):
            return Schema(schema=cur)
        else:
            return cur
    
    def copy(self):
        from copy import deepcopy
        return Schema(schema=deepcopy(self.schema))
        
    '''
    Descriptive rename of unnest, might remove later
    '''
    def get_type(self, path:'Reference') -> 'hqlt.HqlType':
        got = self.unnest(path)
        if isinstance(got, Schema):
            return hqlt.object(got.schema)
        else:
            return got

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
    def strip(self) -> Union['Schema', 'hqlt.HqlType']:
        cur = self.schema
        while isinstance(cur, dict) and len(cur) == 1:
            key = list(cur.keys())[0]
            cur = cur[key]

        if isinstance(cur, dict):
            return Schema(schema=cur)
        else:
            return cur
    
    def rename(self, src:'Reference', dest:'Reference'):
        if not self.assert_field(src):
            raise hqle.QueryException('Attempting to rename a non-existing field')
        
        if self.assert_field(dest):
            raise hqle.QueryException('Attempting to rename field into an existing field')
        
        src_type = self.pop(src)
        
        cur = self.schema
        for idx, i in enumerate(dest):
            # the previous assertion functions guarantee a destination path will work
            # adding to please the linter
            assert isinstance(cur, dict)

            if idx == len(dest) - 1:
                cur[i] = src_type
            else:
                cur = cur[i]
                
    def pop(self, name:'Reference'):
        if not self.assert_field(name):
            raise hqle.QueryException(f'Attempting to pop a non-existing field {name}')
        
        src_type = hqlt.null()
        cur = self.schema
        for idx, i in enumerate(name):
            # the previous assertion function guarantees our path exists
            # adding to please the linter
            assert isinstance(cur, dict)

            if idx == len(name) - 1:
                src_type = cur.pop(i)
            else:
                cur = cur[i]
                
        return src_type

    def drop(self, path:'Reference'):
        def d(path:'Reference', schema:dict, idx:int=0) -> dict:
            new = {}
            for key in schema:
                if key == path[idx]:
                    if idx == len(path) - 1:
                        # Silent drop
                        continue
                    
                    if isinstance(schema[key], dict):
                        rec = d(path, schema[key], idx+1)
                        if rec:
                            new[key] = rec
                
                # Don't have to do anything
                else:
                    new[key] = schema[key]
            return new
                    
        self.schema = d(path, self.schema)
        return self
    
    def drop_many(self, paths:Sequence['Reference']):
        for path in paths:
            self.drop(path)
        return self
    
    '''
    Set a field to a specific type in the schema apply is then expected to be ran
    '''
    def set(self, path:'Reference', htype:Union[CompilerType, "Schema", dict]):
        if isinstance(htype, 'Schema'):
            htype = htype.normalize().schema

        def s(path:'Reference', htype:Union[CompilerType, dict], schema:dict, idx:int=0):
            split = path[idx]

            if idx == len(path) - 1:
                schema[split] = htype
                return schema

            if split in schema:
                schema[split] = s(path, htype, schema[split], idx=idx+1)
            else:
                schema[split] = s(path, htype, {}, idx=idx+1)

            return schema

        self.schema = s(path, htype, self.schema)
        self.normalize()
        return self

    '''
    Generates a schema converted to a given schema target.
    Default is HqlTypes
    '''
    def convert_schema(self, target:str='hql') -> 'Schema':
        from Hql.Types.Hql import HqlTypes as hqlt

        def ce(node:CompilerType, target:str):
            if target == 'hql':
                return node.hql_schema()
            elif target == 'polars':
                return node.pl_schema()
            else:
                raise hqle.CompilerException(f'Unsupported type to convert {node} to {target}')

        def cs(schema:dict, target:str):
            out = dict()
            for key in schema:
                # Not sure if this is needed but I put it there anyways
                '''
                if not schema[key]:
                    target_schema[key] = hqlt.null()
                    continue
                '''
                
                if schema[key] == {}:
                    out[key] = ce(hqlt.object({}), target)
                elif isinstance(schema[key], dict):
                    out[key] = cs(schema[key], target)
                else:
                    out[key] = ce(schema[key], target)
        
            return out

        self.schema = cs(self.schema, target)
        return self
        
    '''
    Generates a schema for use in polars using their types
    Uses structs for nested objects instead of json objects
    '''
    def gen_pl_schema(self) -> pl.DataType:
        from Hql.Types.Hql import HqlTypes as hqlt
        return hqlt.object(self.schema).pl_schema()

    '''
    Gen schema from dicts
    Uses python typing
    '''
    @staticmethod
    def from_json(data:list[dict]) -> 'Schema':
        from Hql.Types.Python import PythonTypes as pyt
        from Hql.Types.Hql import HqlTypes as hqlt

        def from_sample(data:dict) -> pyt.dict:
            new = dict()
            for i in data:
                new[i] = pyt.from_value(data[i])
            return pyt.dict(new)

        # collect groupings of schema
        schemata:set[hqlt.HqlType] = set()
        for i in data:
            hql = from_sample(i).hql_schema()
            schemata.add(hql)

        schema = hqlt.resolve_conflict(list(schemata))

        # Always expect object from dict
        assert isinstance(schema, hqlt.object)
        return Schema(schema=schema)
    
    '''
    Generates a schema using polars typing
    '''
    @staticmethod
    def from_df(df:pl.DataFrame) -> Schema:
        from Hql.Types.Polars import PolarsTypes as plt

        def gen_schema(df:pl.DataFrame) -> hqlt.object:
            schema = dict()
            
            for col in df:
                if isinstance(col.dtype, pl.Struct):
                    schema[col.name] = Schema.from_df(pl.DataFrame(col).unnest(col.name))
                    continue
                
                schema[col.name] = plt.from_pure_polars(col.dtype).hql_schema()
                
            return hqlt.object(schema)

        return Schema(schema=gen_schema(df))

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
    def assert_field(self, field:'Reference'):
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

    def join(self, right:"Schema", on:Sequence['Reference'], kind:str) -> Schema:
        # all of these are semantically the same schema wise
        if kind in ('inner', 'leftsemi', 'rightsemi', 'innerunique', 'leftouter', 'rightouter', 'fullouter'):
            new = self.copy()
            for path, stype in right:
                # change naming for duplicates
                if path in new and path not in on:
                    path[-1] += '_right'
                    new.set(path, stype)

                # No duplicate, matches both sets
                elif path in new and path in on:
                    ...

                # Not yet existing in schema
                elif path not in new:
                    new.set(path, stype)
            
            return new

        elif kind == 'leftanti':
            return self

        elif kind == 'rightanti':
            return right

        else:
            raise hqle.QueryException(f'Invalid join kind {kind} used')
            

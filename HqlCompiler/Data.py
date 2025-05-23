import polars as pl
from HqlCompiler.PolarsTools import PolarsTools as pltools
import HqlCompiler.Types as t
from HqlCompiler.Exceptions import *
import logging

class Data():
    ...

class Table():
    ...

class Schema():
    ...

class Data():
    def __init__(self, tables:list[Table]=None):
        self.tables = tables if tables else []

    def get_table(self, name:str):
        for i in self.tables:
            if i.name == name:
                return i
        return None
    
    def add_table(self, table:Table):
        self.tables.append(table)
        if not self.tables[-1].name:
            self.tables[-1].name = f'Table {len(self.tables)}'

    def to_dict(self):
        dataset = dict()
        for i in self.tables:
            dataset[i.name] = i.to_dicts()

        return dataset

class Table():
    def __init__(self, df:pl.DataFrame=None, init_data:list[dict]=None, schema:Schema=None, name:str=None):
        self.name = name

        if init_data and not schema:
            self.schema = Schema(init_data)
            init_data = self.schema.adjust_mv(init_data)
            self.df = pl.from_dicts(init_data, schema=self.schema.to_pl_schema())
        
        elif init_data and schema:
            self.schema = schema
            self.df = pl.from_dicts(init_data, schema=schema)
        
        elif df and schema:
            self.schema = schema
            self.df = schema.cast_to_schema(df)

        elif df and not schema:
            self.df = df
            logging.warning('Dataframe loaded into table without Hql schema')

        elif schema:
            self.schema = schema

    def change_schema(self, schema:Schema):
        self.df = schema.cast_to_schema(self.df, mv_fields=self.schema.mv_fields)
        self.schema = schema

    def to_dicts(self):
        return self.df.to_dicts()

class Schema():
    def __init__(self, data:list[dict]=None, schema:dict=None):
        # [['foo', 'bar'], ['cat']]
        self.mv_fields = []
        self.schema = dict()

        if data:
            if isinstance(data, list):
                self.schema = self.gen_schema(data)
            else:
                self.schema = self.gen_schema([data])
        elif schema:
            self.schema = schema
        else:
            raise Exception('Attemping to initialize Schema() with no data!')

    # Gets the appropriate Hql type for a particular piece of data
    def to_hql_type(self, proto):
        prototype = type(proto)

        if prototype == dict:
            return prototype
        elif prototype in (list, tuple):
            inner = self.resolve_conflict([self.to_hql_type(x) for x in proto])
            return t.multivalue(inner)
        elif prototype == str:
            return t.string()
        elif prototype == int:
            return t.int()
        elif prototype == float:
            return t.float()
        elif prototype == bool:
            return t.bool()
        elif prototype == type(None):
            return t.null()
        else:
            logging.error(f'Unhandled conversion type {prototype}')

    def to_pl_schema(self, src:dict=None, name:str=None):
        if not src:
            src = self.schema

        schema = {}
        for i in src:
            if name:
                j = src[name]
                i = name
            else:
                j = src[i]
                
            if isinstance(j, dict):
                if len(j) == 0:
                    schema[i] = pl.Struct([])
                else:
                    schema[i] = pl.Struct(self.to_pl_schema(src=j))

            elif isinstance(j, t.multivalue):
                schema[i] = j.pl_schema()

            elif isinstance(j, t.object):
                schema[i] = j.pl_schema()

            else:
                schema[i] = j().pl_schema()

            if name:
                break

        if name:
            return schema[name]
        else:
            return schema

    def resolve_conflict(self, ts:list):
        # Check to see if there's a multivalue we need to handle
        mv = False
        for i in ts:
            if isinstance(i, t.multivalue):
                mv = True
                break
        
        # Handle multivalue
        if mv:
            inner_set = set()
            for i in ts:
                if isinstance(i, t.multivalue):
                    inner_set.add(i.inner)
                else:
                    inner_set.add(i)
            inner = self.resolve_conflict(list(inner_set))
            return t.multivalue(inner)

        l = t.priorities['null']
        for i in [str(x) for x in ts]:
            r = t.priorities[i]
            if l['priority'] > r['priority']:
                continue

            if r['name'] in l['super']:
                l = r
                continue

        return t.types[l['name']]

    def gen_schema(self, data:list[dict]):
        # get a set of keys to handle
        keyset = set()
        for i in data:
            if i:
                keyset |= set(i.keys())
        keyset = list(keyset)

        new = dict()
        for key in keyset:
            typeset = set()
            for datum in data:
                if key not in datum:
                    typeset.add(t.null())
                    continue

                if isinstance(datum[key], dict):
                    typeset.add(dict)
                    continue

                typeset.add(self.to_hql_type(datum[key]))

            # recurse on an object
            if dict in typeset:
                if len(typeset) != 1 and t.null() not in typeset:
                    raise Exception(f"Cannot merge types {list(typeset)}")
                
                sub_data = []
                for i in data:
                    if key in i:
                        sub_data.append(i[key])
                new_schema = Schema(sub_data)

                new[key] = new_schema.schema
                # absorb the new schema's multivalue fields, adding our key onto it
                self.mv_fields += [[key] + x for x in new_schema.mv_fields]

                continue
            
            new[key] = self.resolve_conflict(list(typeset))
            if isinstance(new[key], t.multivalue):
                self.mv_fields.append([key])

        return new
    
    def adjust_mv(self, data:list[dict], mv_fields:list[list[str]]=None):        
        if not mv_fields:
            mv_fields = self.mv_fields

        for field in mv_fields:
            key = field[0]
            if len(field) == 1:
                for row in data:
                    if key not in row:
                        continue

                    if isinstance(row[key], list):
                        continue

                    row[key] = [row[key]]
            else:
                rows = []
                for i in data:
                    if key in i:
                        rows.append(i[key])
                self.adjust_mv(rows, [field[1:]])

        return data
            
    def cast_to_schema(self, data:pl.DataFrame, schema:dict=None, mv_fields:list=None):
        newdf = {}

        schema = schema if schema else self.schema
        mv_fields = mv_fields if mv_fields else self.mv_fields

        for col in data:
            # Base case, we don't specify anything in the target schema
            # so pass through
            if isinstance(schema, dict) and col.name not in schema:
                newdf[col.name] = col
                continue

            # Generic unspecified object
            if schema[col.name] == t.object:
                newdf[col.name] = col
                continue

            # Case to recurse on a nested object
            if col.dtype == pl.Struct:
                subdata = pl.DataFrame(
                    data.select(col.name).unnest(col.name),
                    # schema=self.to_pl_schema(schema)[col.name]
                )

                # advance the multivalue fields to only those applicable to the recurse
                new_fields = []
                for i in mv_fields:
                    if i[0] == col.name:
                        new_fields.append(i[1:])

                newdf[col.name] = self.cast_to_schema(
                    subdata, 
                    schema=schema[col.name],
                    mv_fields=new_fields
                )

                continue


            # See if the current field is designated multi-value
            mv = False
            for i in mv_fields:
                if len(i) == 1 and i[0] == col.name:
                    mv = True

            # mv should always be specified by the schema
            # Unhandled fields are skipped at the top
            if mv:
                intermediate = col.dtype.inner
                target = schema[col.name]().pl_schema()

                if intermediate != target:
                    newdf[col.name] = t.cast(col, pl.List(target))
                else:
                    newdf[col.name] = col

                continue
                

            dtype = col.dtype.inner if isinstance(col.dtype, pl.List) else col.dtype
            if dtype == schema[col.name]().pl_schema():
                newdf[col.name] = col

            newdf[col.name] = col.cast(self.to_pl_schema(src=schema, name=col.name))

        return pl.DataFrame(newdf)
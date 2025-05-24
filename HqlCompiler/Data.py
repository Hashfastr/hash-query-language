import polars as pl
from HqlCompiler.PolarsTools import PolarsTools as plt
from HqlCompiler.Types import HqlTypes as ht
from HqlCompiler.Exceptions import *
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
            return self

        table_groups = dict()

        if not tables_list:
            tables_list = []

        if tables:
            for key in tables:
                tables_list.append(tables[key])

        for i in tables_list:
            if i.name not in table_groups:
                table_groups[i.name] = [i]
            else:
                table_groups[i.name].append(i)

        for name in table_groups:
            # no need to merge, unique table
            if len(table_groups[name]) == 1:
                self.tables[name] = table_groups[name][0]
                continue

            self.tables[name] = Table.merge(table_groups[name])

    def __len__(self):
        length = 0
        for i in self.tables:
            length += len(self.tables[i])
        return length

    def get_table(self, name:str):
        if name in self.tables:
            return self.tables[name]
        return None
    
    def add_table(self, table:Table):
        tables = [table]
        if table.name in self.tables:
            tables.append(self.tables.pop(table.name))

        if len(tables) != 1:
            new = Table.merge(tables)
        else:
            new = tables[0]

        self.tables[new.name] = new

    def get_elements(self, fields:list[list[str]]):
        tables = []
        for i in self.tables:
            tables.append(self.tables[i].get_elements(fields))

        return Data(tables_list=tables)

    def to_dict(self):
        dataset = dict()
        for i in self.tables:
            dataset[i] = self.tables[i].to_dicts()

        return dataset
    
    def merge(data:list[Data]):
        tables = []
        for datum in data:
            for name in datum.tables:
                tables.append(datum.tables[name])

        return Data(tables_list=tables)

class Table():
    def __init__(self, df:pl.DataFrame=None, init_data:list[dict]=None, schema:Schema=None, name:str=None):
        self.name = name
        self.df = None
        self.schema = None

        if init_data and not schema:
            self.schema = Schema(init_data)
            init_data = self.schema.adjust_mv(init_data)
            self.df = pl.from_dicts(init_data, schema=self.schema.to_pl_schema())
        
        elif init_data and schema:
            self.schema = schema
            self.df = pl.from_dicts(init_data, schema=schema)
        
        elif not df.is_empty() and schema:
            self.schema = schema
            self.df = schema.cast_to_schema(df)

        elif not df.is_empty() and not schema:
            self.df = df
            logging.warning('Dataframe loaded into table without Hql schema')

        elif schema:
            self.schema = schema

    def __len__(self):
        return len(self.df)

    def merge(tables:list[Table]=None):
        dfs = []
        schemata = []
        for table in tables:
            if table.df:
                dfs.append(table.df)

                if table.schema:
                    schemata.append(table.scheme)

        df = plt.merge(dfs)
        schema = Schema.merge(schemata)

        return Table(df=df, schema=schema, name=tables[0].name)

    def change_schema(self, schema:Schema):
        self.df = schema.cast_to_schema(self.df, mv_fields=self.schema.mv_fields)
        self.schema = schema

    def to_dicts(self):
        return self.df.to_dicts()
    
    # Takes in a list of paths
    # [['foo', 'bar'], ['client', 'ip', 'src']]
    # Returns a Table with the subset of the data
    def get_elements(self, fields:list[list[str]]):
        dfs = []
        for field in fields:
            dfs.append(plt.get_element(self.df, field))

        df = plt.merge(dfs)
        schema = self.schema.extract_schema(fields)

        return Table(df, schema=schema, name=self.name)

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

        return new

    # Extract the schema for a given set of fields
    def extract_schema(self, fields:list[list[str]], schema:dict=None):
        schema = schema if schema else self.schema

        new = dict()
        for field in fields:
            if len(field) == 1:
                new[field[0]] = schema[field[0]]
                continue

            new[field[0]] = self.extract_schema([field[1:]], schema=schema[field[0]]).schema

        return Schema(schema=new)

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

            elif isinstance(j, ht.multivalue):
                schema[i] = j.pl_schema()

            elif isinstance(j, ht.object):
                schema[i] = j.pl_schema()

            else:
                schema[i] = j().pl_schema()

            if name:
                break

        if name:
            return schema[name]
        else:
            return schema

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
                    typeset.add(ht.null())
                    continue

                if isinstance(datum[key], dict):
                    typeset.add(dict)
                    continue

                typeset.add(ht.to_hql_type(proto=datum[key]))

            # recurse on an object
            if dict in typeset:
                if len(typeset) != 1 and ht.null() not in typeset:
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
            
            new[key] = ht.resolve_conflict(list(typeset))
            if isinstance(new[key], ht.multivalue):
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
            if schema[col.name] == ht.object:
                newdf[col.name] = col
                continue

            # Case to recurse on a nested object
            if col.dtype == pl.Struct: # or isinstance(schema[col.name], dict):
                # print(json.dumps(schema[col.name], indent=2, default=repr))
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
                    newdf[col.name] = ht.cast(col, pl.List(target))
                else:
                    newdf[col.name] = col

                continue

            dtype = col.dtype.inner if isinstance(col.dtype, pl.List) else col.dtype

            if dtype == schema[col.name]().pl_schema():
                newdf[col.name] = col

            newdf[col.name] = col.cast(self.to_pl_schema(src=schema, name=col.name))

        return pl.DataFrame(newdf)
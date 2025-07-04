from .Table import Table
from .Schema import Schema
from .Series import Series
from HqlCompiler.Exceptions import *
import logging
from HqlCompiler.Types.Hql import HqlTypes as hqlt

class Data():
    # tables is a unique list of tables by name
    # tables is a non-unique list of tables.
    def __init__(self, tables:list[Table]=None):
        self.tables = dict()

        # empty base case
        if not tables:
            return

        table_groups = dict()

        for table in tables:
            if not isinstance(table, Table):
                raise CompilerException('Non-table passed to Data as init data')

        # Give names to names-less tables
        for idx, i in enumerate(tables):
            if i.name == None:
                i.name = f'Table {idx}'

        # Form table groups for merging
        for i in tables:
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

        return Data(tables=tables)
    
    def unnest(self, field:list[str]):
        tables = []
        for table in self:
            new = table.unnest(field)
            
            if isinstance(new, Series):
                new = Table(series=new, name=table.name)
            
            tables.append(new)
        
        return Data(tables=tables)

    def to_dict(self):
        dataset = dict()
        
        dataset['data'] = {}
        for table in self:
            dataset['data'][table.name] = table.to_dicts()
            
        dataset['schema'] = self.get_schema()

        return dataset
   
    @staticmethod
    def merge(data:list["Data"]):
        if len(data) == 1:
            return data[0]
        
        tables = []
        for datum in data:
            for table in datum:
                tables.append(table)

        return Data(tables=tables)

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

    def join(self, right:"Data", on:str, kind:str='innerunique'):
        tables = []
        for lt in self:
            new = []
            for rt in right:
                new.append(lt.join(rt, on, kind))

            tables.append(Table.concat(new))
        
        return Data(tables=tables)
    
    def strip(self):
        new = []
        for table in self:
            new.append(table.strip())
        return Data(tables=new)

    def drop_many(self, paths:list[list[str]]):
        cur = self
        for path in paths:
            cur = cur.drop(path)
        return cur

    def drop(self, path:list[str]):
        new = []
        for table in self:
            new.append(table.drop(path))
        return Data(tables=new)

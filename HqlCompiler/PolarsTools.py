import polars as pl
import logging

class pltools():
    def advance(columns:list[pl.DataFrame]) -> list[pl.DataFrame]:
        new = []
        name = columns[0].columns[0]
        for i in columns:
            new.append(i.select(name).unnest(name))
            
        return new

    def merge(dataframes:list[pl.DataFrame]):
        columns = {}
        for i in dataframes:
            if len(i.columns) == 0:
                continue
           
            name = i.columns[0]
            
            if name not in columns:
                columns[name] = []
            
            columns[name].append(i)
            
        mergable = []
        for i in columns:
            if len(columns[i]) == 1:
                mergable += columns[i]
                continue

            new = pl.DataFrame({i: pltools.merge(pltools.advance(columns[i])).to_struct()})

            mergable.append(new)
            
        return pl.concat(mergable, how="horizontal")

    # Fields is a list of the given path names.
    # host.name -> ['host', 'name']
    # Returns a df representation of that field, maintains nested-ness
    def get_element(data:pl.DataFrame, fields:list[str], index:int=0):
        if index == len(fields):
            return pl.DataFrame({fields[index-1]: data.to_struct()})
        
        split = fields[index]
    
        if split not in data:
            return pl.DataFrame({})

        new = data.select(split)
        
        if len(fields) == 1:
            return new
            
        if isinstance(new[split].dtype, pl.Struct):
            new = new.unnest(split)
        else:
            return pl.DataFrame({fields[index-1]: new.to_struct()})
            
        rec_data = pltools.get_element(new, fields, index + 1)
        
        if index == 0:
            return rec_data
        else:
            return pl.DataFrame({fields[index-1]: rec_data.to_struct()})
    
    # Gets the value of an element, does not preserve df structure
    # Just returns the value
    # So for a base value, a series, and for a field that's a struct, a struct dataframe.
    def get_element_value(data:pl.DataFrame, fields:list[str], index:int=0):
        # if not fields:
        #     split = data.columns[0]
        # else:
        #     split = fields[index]
                
        split = fields[index]

        if split not in data:
            if index == 0:
                raise Exception(f"Invalid field referenced {split}")
            else:
                raise Exception(f"Invalid field {split} in path {'.'.join(fields)}")
        
        new = data.select(split)
        
        if fields and len(fields) == 1:
            if new[split].dtype == pl.Struct:
                return pl.DataFrame(new.unnest(split))
            
            return new.to_series()
        
        if isinstance(new[split].dtype, pl.Struct):
            new = new.unnest(split)
        else:
            return new.to_series()
        
        return pltools.get_element_value(new, fields, index + 1)
    
    def build_element(name:list[str], data):
        if len(name) == 1:
            return pl.DataFrame({name[0]: data})
        
        new = pltools.build_element(name[1:], data)
        return pl.DataFrame({name[0]: new.to_struct()})
    
    def assert_field(data:pl.DataFrame, field:list[str], index:int=0) -> bool:
        split = field[index]

        if split not in data:
            return None
        
        new = data.select(split)
        
        if len(field) == 1:            
            return field
        
        if isinstance(new[split].dtype, pl.Struct):
            new = new.unnest(split)
        else:
            return field
                
        return pltools.assert_field(new, field, index + 1)

    def path_to_expr(path:list[str]):
        expr = pl
        for idx, i in enumerate(path):
            if idx == 0:
                expr = expr.col(i)
            else:
                expr = expr.struct.field(i)

        return expr

    def build_filter(ctx, expr):
        if expr.type == 'Equality':
            lh = expr.lh.eval(ctx, as_pl=True)    
            rh = expr.rh.eval(ctx, as_pl=True)
            return (lh == rh)
        else:
            logging.warning(f'Unimplemented filter expression type {expr.type}')

import polars as pl

class PolarsTools():
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
                mergable.append(columns[i][0])
                continue

            new = pl.DataFrame({i: PolarsTools.merge(PolarsTools.advance(columns[i])).to_struct()})

            mergable.append(new)
            
        return pl.concat(mergable, how="horizontal")

    # Fields is a list of the given path names.
    # host.name -> ['host', 'name']
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
            
        rec_data = PolarsTools.get_element(new, fields, index + 1)
        
        if index == 0:
            return rec_data
        else:
            return pl.DataFrame({fields[index-1]: rec_data.to_struct()})
        
    def get_element_value(data:pl.DataFrame, fields:list[str]=None, index:int=0):
        if not fields:
            split = data.columns[0]
        else:
            split = fields[index]

        if split not in data:
            if index == 0:
                raise Exception(f"Invalid field referenced {split}")
            else:
                raise Exception(f"Invalid field {split} in path {'.'.join(fields[:index])}")
        
        new = data.select(split)
        
        if fields and len(fields) == 1:
            if new[split].dtype == pl.Struct:
                return pl.DataFrame(new.unnest(split))
            
            return new.to_series()
        
        if isinstance(new[split].dtype, pl.Struct):
            new = new.unnest(split)
        else:
            return new.to_series()
        
        return PolarsTools.get_element_value(new, fields, index + 1)
    
    def build_element(name:list[str], data):
        if len(name) == 1:
            return pl.DataFrame({name[0]: data})
        
        new = PolarsTools.build_element(name[1:], data)
        return pl.DataFrame({name[0]: new.to_struct()})
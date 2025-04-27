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

    def get_element(data:pl.DataFrame, fields:list[str], index:int=0):
        if index == len(fields):
            return pl.DataFrame({fields[index-1]: data.to_struct()})
        
        split = fields[index]

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
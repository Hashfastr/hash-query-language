import polars as pl

class pltools():
    @staticmethod
    def advance(columns:list[pl.DataFrame]) -> list[pl.DataFrame]:
        new = []
        name = columns[0].columns[0]
        for i in columns:
            new.append(i.select(name).unnest(name))
            
        return new

    @staticmethod
    def merge(dfs:list[pl.DataFrame]):
        # Get counts for each column, knowing where we have conflicts.
        columns = {}
        for df in dfs:
            if len(df.columns) == 0:
                continue
            
            # count and collect columns
            for col in df:
                if col.name not in columns:
                    columns[col.name] = []
                    
                columns[col.name].append(col)

        mergable = []
        for i in columns:
            if len(columns[i]) == 1:
                mergable.append(pl.DataFrame({i: columns[i][0]}))
                continue

            raise Exception('unhandled merge case')
                
            #new = pl.DataFrame({i: pltools.merge(pltools.advance(columns[i])).to_struct()})

            #mergable.append(new)
                        
        return pl.concat(mergable, how="horizontal")

    # Fields is a list of the given path names.
    # host.name -> ['host', 'name']
    # Returns a df representation of that field, maintains nested-ness
    @staticmethod
    def get_element(df:pl.DataFrame, path:list[str]):
        expr = pltools.path_to_expr(path)
        return df.select(expr)

    # Gets the value of an element, does not preserve df structure
    # Just returns the value
    # So for a base value, a series, and for a field that's a struct, a struct dataframe.
    @staticmethod
    def get_element_value(df:pl.DataFrame, path:list[str]):
        expr = pltools.path_to_expr_value(path)
        data = df.select(expr)
        
        if isinstance(data.dtypes[0], pl.Struct):
            return data.unnest(path[-1])
        else:
            return data.to_series()
    
    @staticmethod
    def build_element(name:list[str], data):
        if len(name) == 1:
            return pl.DataFrame({name[0]: data})
        
        new = pltools.build_element(name[1:], data)
        return pl.DataFrame({name[0]: new.to_struct()})

    @staticmethod
    def path_to_expr_value(path:list[str]):
        # build selector
        expr = pl.col(path[0])
        for i in path[1:]:
            expr = expr.struct.field(i)
            
        return expr

    @staticmethod
    def path_to_expr(path:list[str]):
        expr = pltools.path_to_expr_value(path)
        
        # rebuild object
        for i in path[::-1][1:]:
            expr = pl.struct(expr).alias(i)

        return expr

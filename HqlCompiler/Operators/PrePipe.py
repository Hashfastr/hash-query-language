from .Operator import Operator
from HqlCompiler.Expression import Expression, StringLiteral
import polars as pl
from ..PolarsTools import PolarsTools as pltools
from HqlCompiler.Context import register_op, Context
from HqlCompiler.Functions import Function
import HqlCompiler.Config as Config

import logging
from HqlCompiler.Exceptions import *

# Super meta operator, 
@register_op('PrePipe')
class PrePipe(Operator):
    def __init__(self, expr:Expression):
        super().__init__()
        self.expr = expr
        self.non_conseq = []
        
    def resolve_tabular_path(self, ctx:Context, expr:Expression):
        funcs = []
        
        if expr.type == 'Path':
            path = expr.path
        else:
            path = [expr]
        
        # This if else block handles the first element of the path
        # Tabular expression is just database('xyz') or index('xyz')
        # Up to the database driver to decide what to do with no index specification
        # Can be added onto later
        # Ensures there's a database function at top level
        if path[0].type == "DotCompositeFunction":                
            path_funcs = path[0].eval(ctx, no_exec=True)
            if path_funcs[0].name != 'database':
                funcs.append(ctx.get_func('database')([]))
            funcs += path_funcs
        
        # Tabular expression just giving a database name, e.g. ['tf11-elastic']
        elif len(path) == 1:
            funcs.append(ctx.get_func('database')([]))
            funcs.append(ctx.get_func('index')(path))
        
        # handle the case of an identifier with another path element afterwards
        else:
            funcs.append(ctx.get_func('database')([path[0]]))

        # A tabular expression specifying something like:
        # database("tf11-elastic").['so-beats-2022.10.*']
        # Handles the second element of the path
        if len(path) == 2:
            # Tabular expression is just database('xyz') or index('xyz')
            # Up to the database driver to decide what to do with no index specification
            if path[1].type == "DotCompositeFunction":                
                path_funcs = path[1].eval(ctx, no_exec=True)
                funcs += path_funcs
                
            # Tabular expression just giving a index name, e.g. ['so-beats-2022.10.*']
            else:
                funcs.append(ctx.get_func('index')([path[1]]))
            
        if len(path) > 2:
            raise CompilerException('Invalid path reference for tabular expression')

        return funcs
        
    def eval(self, ctx:Context, **kwargs):
        tabular = kwargs.get('tabular', False)
        receiver = None
        
        if tabular:
            funcs = self.resolve_tabular_path(ctx, self.expr)
            for i in funcs:
                receiver = i.eval(ctx, receiver=receiver)
            return receiver
        
        return None
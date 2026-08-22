from __future__ import annotations
from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_func
from typing import TYPE_CHECKING, Optional, Union

if TYPE_CHECKING:
    from Hql.Context import Context

# This is a meta function resolved while parsing
@register_func('index')
class index(Function):
    def __init__(self, args:list, conf:Optional[dict]=None):
        from Hql.Expressions.Literals import StringLiteral
        from Hql.Expressions.References import Reference

        Function.__init__(self, args, 1, 1)

        name = self.args[0]
        if not isinstance(name, (StringLiteral, Reference)):
            raise hqle.ArgumentException(f'Bad database index argument datatype {args[0].type}')
        self.name:Union[StringLiteral, Reference] = name
    
    def preprocess(self, ctx: Context, receiver=None) -> object:
        from Hql.Expressions.Literals import StringLiteral
        
        name = self.name.preprocess(ctx)
        if not isinstance(name, StringLiteral):
            raise hqle.QueryException(f'File function give argument that doesn\'t resolve to string literal: {type(name)}')

        self.name = name

        return self
        
    def eval(self, ctx: Context, receiver=None) -> object:
        from Hql.Database import Database

        db = receiver
        index_name = self.name.str()
        
        if not db:
            db = ctx.get_func('database')([]).eval(ctx)
        
        if issubclass(type(db), Database):
            db.add_index(index_name)
        else:
            raise hqle.CompilerException(f'Function {self.name} cannot be called on {type(db)}')
        
        return db

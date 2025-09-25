from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql import Config
from Hql.Context import register_func, Context
from Hql.Expressions import StringLiteral

# This is a meta function resolved while parsing
@register_func('index')
class index(Function):
    def __init__(self, args:list):
        Function.__init__(self, args, 1, 1)
        self.preprocess = True

        if not isinstance(self.args[0], StringLiteral):
            raise hqle.ArgumentException(f'Bad database index argument datatype {args[0].type}')
        
    def eval(self, ctx:'Context', **kwargs):
        from Hql.Operators.Database import Database

        db = kwargs.get('receiver', None)
        index_name = self.args[0].eval(ctx, as_str=True)
        
        if not db:
            db = ctx.get_func('database')([]).eval(ctx)
        
        if issubclass(type(db), Database):
            db.add_index(index_name)
        else:
            raise hqle.CompilerException(f'Function {self.name} cannot be called on {type(db)}')
        
        return db

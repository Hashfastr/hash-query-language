from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql import Config
from Hql.Context import register_func, Context
from Hql.Expressions import StringLiteral

# This is a meta function resolved while parsing
@register_func('http')
class http(Function):
    def __init__(self, args:list):
        Function.__init__(self, args, 1, -1)
        self.preprocess = True

        for i in args:
            if not isinstance(i, StringLiteral):
                raise hqle.QueryException(f'Invalid argument type passed to macro function: {type(i)}')
        
    def eval(self, ctx:'Context', **kwargs):
        from Hql.Operators.Database import Database

        db = kwargs.get('receiver', None)
        urls = [x.eval(ctx, as_str=True) for x in self.args]
        
        if not db:
            dbconf = ctx.config.get_default_db()
            db = ctx.get_db(dbconf['type'])(dbconf, name='default')
        
        if db and issubclass(type(db), Database) and db.has_method(self.name):
            db.urls += urls
        else:
            raise hqle.CompilerException(f'Function {self.name} cannot be called on {type(db)}')

        
        return db

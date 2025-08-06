from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql import Config
from Hql.Context import register_func, Context

# This is a meta function resolved while parsing
@register_func('index')
class index(Function):
    def __init__(self, args:list):
        super().__init__(args, 1, 1)

        if self.args[0].type not in ('StringLiteral', 'EscapedName'):
            raise hqle.ArgumentException(f'Bad database argument datatype {args[0].type}')
        
    def eval(self, ctx:'Context', **kwargs):
        from Hql.Operators.Database import Database

        db = kwargs.get('receiver', None)
        index_name = self.args[0].eval(ctx, as_str=True)
        
        if not db:
            dbconf = Config.HqlConfig.get_default_db()
            db = ctx.get_db(dbconf['TYPE'])(dbconf)
        
        if db and issubclass(type(db), Database):
            db.add_index(index_name)
        else:
            raise hqle.CompilerException(f'Function {self.name} cannot be called on {type(db)}')
        
        return db

from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql import Config
from Hql.Context import register_func, Context
from Hql.Expressions import PipeExpression, StringLiteral, Expression, DotCompositeFunction
from Hql.Compiler import InstructionSet, HqlCompiler

@register_func('macro')
class macro(Function):
    def __init__(self, args:list):
        Function.__init__(self, args, 1, -1)
        self.preprocess = True

        for i in args:
            if not isinstance(i, StringLiteral):
                raise hqle.QueryException(f'Invalid argument type passed to macro function: {type(i)}')

    def parse_macro(self, macro:dict, src:str) -> Expression:
        from Hql.Parser import Parser
        from Hql.Expressions import Expression

        if 'hql' not in macro:
            raise hqle.ConfigException(f'Missing hql definition in config {src}')

        parser = Parser(macro['hql'], f'{src}')
        parser.assemble(targets=['pipeExpression', 'beforePipeExpression', 'emptyPipedExpression'])
        assert isinstance(parser.assembly, Expression)

        return parser.assembly
        
    def eval(self, ctx:'Context', **kwargs):
        db = kwargs.get('receiver', None)
        macros = [x.eval(ctx, as_str=True) for x in self.args]
        compiler = HqlCompiler(ctx.config)
        
        if not db:
            dbconf = ctx.config.get_default_db()
            db = ctx.get_db(dbconf['type'])(dbconf, name='default')

        upstream = []
        for i in macros:
            macro = db.get_macro(i)
            if not macro:
                raise hqle.QueryException(f'Macro not found: {i}')
            parsed = self.parse_macro(macro, f'{db.name}/{i}')

            if not isinstance(parsed, PipeExpression):
                parsed = PipeExpression([], prepipe=parsed)

            acc, rej = compiler.compile(parsed)
            upstream.append(acc)

        return InstructionSet(upstream)

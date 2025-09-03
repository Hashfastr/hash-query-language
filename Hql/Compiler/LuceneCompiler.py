from Hql.Exceptions import HqlExceptions as hqle
from typing import Callable, Union, TYPE_CHECKING
from . import Compiler, HqlCompiler

if TYPE_CHECKING:
    import Hql
    from Hql.Expressions import Expression
    from Hql.Compiler import BranchDescriptor

class LuceneCompiler(Compiler):
    def __init__(self) -> None:
        Compiler.__init__(self)
        self.attrs = {
            'nested_objects': True,
            'wildcards': True,
            'wildcard_names': True,
            'complex_names': True,
            'row_reducing': True,
            'regex_matching': True,
            'regex_insensitive': False,
            'regex_multiline': False,
            'regex_dotall': False,
            'regex_global': False
        }
        self.expr = None

    '''
    def add_op(self, op: 'BranchDescriptor') -> Union['BranchDescriptor', None]:
        from Hql.Operators import Where

        if not op.op:
            return op

        if isinstance(op.op, Where):
            op.compatible(self.attrs)

        return 
    '''

    def Where(self, op:'Hql.Operators.Where', preprocess:bool=True) -> tuple[Union[None, 'Hql.Operators.Where', str], Union[None, 'Hql.Operators.Where', str]]:
        from Hql.Operators import Where
        res = self.compile(op.expr, preprocess=preprocess)

        if preprocess and res:
            assert isinstance(res, Expression)
            return Where(res, op.parameters), None

        assert isinstance(res, (type(None), str))
        return res, None
        
    def BinaryLogic(self, expr: 'Hql.Expressions.BinaryLogic', preprocess: bool = True) -> tuple[Union[None, 'Hql.Expressions.BinaryLogic', str], Union[None, 'Hql.Expressions.BinaryLogic', str]]:
        from Hql.Expressions import BinaryLogic

        exprs = [expr.lh] + expr.rh
        if expr.bitype == 'and':
            bitok = ' AND '
        else:
            bitok = ' OR '

        ret = bitok.join([get_expr(x)(x) for x in exprs])
        return f'({ret})', None

compiler_registry = {}
def get_expr(expr:"Hql.Expressions.Expression"):
    expr_str = f'{expr.type}_expr'

    if expr_str in compiler_registry:
        return compiler_registry[expr_str]

    raise hqle.CompilerException(f'Attempting to compile unimplemented parse object {expr.type}')

def register(name:str):
    def decorator(func):
        compiler_registry[name] = func
        return func
    return decorator

@register('Where_op')
def Where_op(op:"Hql.Operators.Where") -> str:
    if op.expr == None:
        return ''
    return get_expr(op.expr)(op.expr)

@register('StringLiteral_expr')
def StringLiteral_expr(expr:"Hql.Expressions.StringLiteral") -> str:
    return f'"{expr.value}"'

@register('Integer_expr')
@register('Float_expr')
def Float_expr(expr:"Hql.Expressions.Float") -> str:
    return f'{expr.value}'

@register('Bool_expr')
def Bool(expr:"Hql.Expressions.Bool") -> str:
    return 'True' if expr.value else 'False'

@register('Keyword_expr')
@register('Identifier_expr')
def BasicIdentifier(expr:"Hql.Expressions.NamedReference") -> str:
    if expr.name == None:
        raise hqle.CompilerException('NamedReference has null value')
    return expr.name

@register('EscapedNamedReference_expr')
def EscapedName(expr:"Hql.Expressions.EscapedNamedReference") -> str:
    if expr.name == None:
        raise hqle.CompilerException('NamedReference has null value')
    return f'\"{expr.name}\"'

@register('Path_expr')
def Path(expr:"Hql.Expressions.Path") -> str:
    path = [get_expr(x)(x) for x in expr.path]
    return '.'.join(path)

@register('Equality_expr')
def Equality(expr:"Hql.Expressions.Equality") -> str:
    lh = get_expr(expr.lh)(expr.lh)
    
    exprs = []
    for i in expr.rh:
        rh = get_expr(i)(i)
        ret = f'{lh}:{rh}'
        exprs.append(ret)

    ret = ' OR '.join(exprs)
    if len(exprs) > 1:
        ret = f'({ret})'

    return f'(NOT {ret})' if expr.neq else ret

@register('Relational_expr')
def Relational(expr:"Hql.Expressions.Relational") -> str:
    lh = get_expr(expr.lh)(expr.lh)
    rh = get_expr(expr.rh[0])(expr.rh[0])
    return f'{lh}:{expr.op}{rh}'

@register('BetweenEquality_expr')
def Between(expr:"Hql.Expressions.BetweenEquality") -> str:
    lh = get_expr(expr.lh)(expr.lh)
    start = get_expr(expr.start)(expr.start)
    end = get_expr(expr.end)(expr.end)

    ret = f'{lh}:[{start} TO {end}]'

    if expr.negate:
        return f'(NOT {ret})'
    else:
        return ret



@register('BasicRange_expr')
def Range(expr:"Hql.Expressions.BasicRange") -> str:
    start = get_expr(expr.start)(expr.start)
    end = get_expr(expr.end)(expr.end)
    return f'[{start} TO {end}]'

@register('Regex_expr')
def Regex(expr:"Hql.Expressions.Regex") -> str:
    lh = get_expr(expr.lh)(expr.lh)
    rh = get_expr(expr.rh)(expr.rh)
    return f'{lh}:/{rh}/'

@register('Substring_expr')
def Substring(expr:"Hql.Expressions.Substring") -> str:
    lh = get_expr(expr.lh)(expr.lh)

    rhs = []
    for i in expr.rh:
        rhs.append(get_expr(i)(i))

    exprs = []
    for i in rhs:
        if 'startswith' in expr.op or 'prefix' in expr.op:
            exprs.append(f'{lh}:/{i}.*/')
        elif 'endswith' in expr.op or 'suffix' in expr.op:
            exprs.append(f'{lh}:/.*{i}/')
        else:
            exprs.append(f'{lh}:/.*{i}.*/')

    if 'all' in expr.op:
        ret = ' AND '.join(exprs)
    else:
        ret = ' OR '.join(exprs)
    ret = f'({ret})'

    if expr.neq:
        ret = f'NOT {ret}'

    return ret

from Hql.Exceptions import HqlExceptions as hqle
from typing import Callable, Union, TYPE_CHECKING

if TYPE_CHECKING:
    import Hql.Expressions as Expr
    import Hql.Operators as Ops

func_temp = Callable[[Union["Ops.Operator", "Expr.Expression"]], str]

compiler_registry = {}
def get_func(expr:"Expr.Expression") -> func_temp:
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
def Where_op(op:"Ops.Where") -> str:
    if op.expr == None:
        return ''
    return get_func(op.expr)(op.expr)

@register('StringLiteral_expr')
def StringLiteral_expr(expr:"Expr.StringLiteral") -> str:
    return f'"{expr.value}"'

@register('Integer_expr')
@register('Float_expr')
def Float_expr(expr:"Expr.Float") -> str:
    return f'{expr.value}'

@register('Bool_expr')
def Bool(expr:"Expr.Bool") -> str:
    return 'True' if expr.value else 'False'

@register('Keyword_expr')
@register('Identifier_expr')
def BasicIdentifier(expr:"Expr.NamedReference") -> str:
    if expr.name == None:
        raise hqle.CompilerException('NamedReference has null value')
    return expr.name

@register('EscapedNamedReference_expr')
def EscapedName(expr:"Expr.EscapedNamedReference") -> str:
    if expr.name == None:
        raise hqle.CompilerException('NamedReference has null value')
    return f'\"{expr.name}\"'

@register('Path_expr')
def Path(expr:"Expr.Path") -> str:
    path = [get_func(x)(x) for x in expr.path]
    return '.'.join(path)

@register('Equality_expr')
@register('CaseInsensitiveStringCmp_expr')
def Equality(expr:"Expr.Equality") -> str:
    lh = get_func(expr.lh)(expr.lh)
    rh = get_func(expr.rh)(expr.rh)

    ret = f'{lh}:{rh}'

    return f'(NOT {ret})' if expr.neq else ret

@register('ListEquality_expr')
def ListEquality(expr:"Expr.ListEquality") -> str:
    lh = get_func(expr.lh)(expr.lh)

    rh = ' or '.join([get_func(x)(x) for x in expr.rh])
    rh = f'({rh})'
    
    ret = f'{lh}: {rh}'

    if expr.op == 'in':
        return ret
    else:
        return f'(NOT {ret})'

@register('Relational_expr')
def Relational(expr:"Expr.Relational") -> str:
    lh = get_func(expr.lh)(expr.lh)
    rh = get_func(expr.rh)(expr.rh)
    return f'{lh} {expr.eqtype} {rh}'

@register('BetweenEquality_expr')
def Between(expr:"Expr.BetweenEquality") -> str:
    lh = get_func(expr.lh)(expr.lh)
    start = get_func(expr.start)(expr.start)
    end = get_func(expr.end)(expr.end)

    ret = f'{lh}:[{start} TO {end}]'

    if expr.negate:
        return f'(NOT {ret})'
    else:
        return ret

@register('BinaryLogic_expr')
def Binary(expr:"Expr.BinaryLogic") -> str:
    exprs = [expr.lh] + expr.rh
    if expr.bitype == 'and':
        bitok = ' and '
    else:
        bitok = ' or '

    ret = bitok.join([get_func(x)(x) for x in exprs])
    return f'({ret})'

@register('BasicRange_expr')
def Range(expr:"Expr.BasicRange") -> str:
    start = get_func(expr.start)(expr.start)
    end = get_func(expr.end)(expr.end)
    return f'[{start} TO {end}]'

@register('Regex_expr')
def Regex(expr:"Expr.Regex") -> str:
    lh = get_func(expr.lh)(expr.lh)
    rh = get_func(expr.rh)(expr.rh)
    return f'{lh}:/{rh}/'

@register('Contains_expr')
def Contains(expr:"Expr.Contains") -> str:
    lh = get_func(expr.lh)(expr.lh)
    rh = get_func(expr.rh)(expr.rh)
    
    if expr.startswith:
        ret = f'{lh}:/{rh}.*/'
    elif expr.endswith:
        ret = f'{lh}:/.*{rh}/'
    else:
        ret = f'{lh}:/.*{rh}.*/'

    if expr.neq:
        ret = f'(NOT {ret})'

    return ret

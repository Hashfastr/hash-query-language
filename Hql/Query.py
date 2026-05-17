import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Expressions import Expression, PipeExpression
    from Hql.Context import Context

# Top most object, a query.
# Comprised of multiple statements
#
# let AttackerIPs = syslog-*
# | where program == "sshd" and user == "hashfastr" and status == "Accepted"
# | project IP;
# syslog-*
# | where program == "sshd" and status == "Accepted"
# | join kind=inner (AttackerIPs) on IP
# | project timestamp, user, IP, authtype
#
# Has two statements, AttackerIPs, and the root statement.
# Each statement is denoted by a ; with the exception of the root statement.
# The root statement is denoted by EOF, but can have a ; regardless
class Query():
    def __init__(self, statements:list['Statement']):
        self.statements = statements

    def deparse(self):
        statements = []
        for i in self.statements:
            statements.append(i.deparse())
        return '\n;\n'.join(statements)

    def to_dict(self):
        return {
            "statements": [x.to_dict() for x in self.statements]
        }

    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)

# Generic for a statement, see children as this can be very diverse
class Statement():
    def __init__(self):
        self.type = self.__class__.__name__
    
    def to_dict(self) -> dict:
        return {
            'type': self.type,
        }

    def deparse(self) -> str:
        return ''
    
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)

class QueryStatement(Statement):
    def __init__(self, root:'PipeExpression'):
        Statement.__init__(self)
        self.root = root

    def to_dict(self):
        out = super().to_dict()
        out['query'] = self.deparse()
        return out

    def deparse(self):
        return self.root.deparse()

class LetStatement(Statement):
    def __init__(self, name:'Expression', value:'PipeExpression', macro:bool=False):
        Statement.__init__(self)
        self.root = value
        self.name = name
        self.macro = macro
        
    def to_dict(self):
        return {
            'type': self.type,
            'macro': self.macro,
            'name': self.name.to_dict(),
            'value': self.root.to_dict()
        }

    def deparse(self):
        name = self.name.deparse()
        value = self.root.deparse()
        return f'let {name} = {value}'
        
    def eval(self, ctx:'Context') -> 'Context':
        name = self.name.str()
        
        if self.macro:
            ctx.macros[name] = self.root
        else:
            ctx.symbol_table[name] = self.root

        return ctx

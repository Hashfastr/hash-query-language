import json
from HqlCompiler.Expression import Expression
from HqlCompiler.Context import Context

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
    def __init__(self):
        self.statements = []

    def to_dict(self):
        return {
            "statements": [x.to_dict() for x in self.statements]
        }

    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)

# Generic for a statement, see children as this can be very diverse
class Statement():
    def __init__(self, root):
        self.type = self.__class__.__name__
        self.root = root
    
    def to_dict(self):
        return {
            'type': self.type,
            'root': self.root.to_dict()
        }
    
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)

class QueryStatement(Statement):
    def __init__(self, root):
        Statement.__init__(self, root)

class LetStatement(Statement):
    def __init__(self, name:Expression, value:Expression, lettype:str):
        Statement.__init__(self, value)
        self.name = name
        self.lettype = lettype
        
    def to_dict(self):
        return {
            'type': self.type,
            'lettype': self.lettype,
            'name': self.name.to_dict(),
            'value': self.root.to_dict()
        }
        
    def eval(self, ctx:Context, **kwargs):
        name = self.name.eval(ctx, as_str=True)
                
        if kwargs.get('no_exec', False):
            ctx.symbol_table[name] = self.root
        else:
            ctx.symbol_table[name] = self.root.eval(ctx)

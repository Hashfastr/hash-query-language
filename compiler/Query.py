import json

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

# See above comments for the Query class for explaination on statements
# in relation to a query.
# Each statement is itself a chain of processing, that is, it is self contained.
# The results of a particular statement can be used in another, hence the name.
# The root statement has the name of "".
# In the example put above the Query class, there are two statements
# "AttackerIPs" and ""
class Statement():
    def __init__(self, name:str=""):
        # if empty it's the prime statement
        self.name = name
        self.operations = []
    
    def to_dict(self):
        return {
            'name': self.name,
            'operations': [x.to_dict() for x in self.operations]
        }
    
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
    
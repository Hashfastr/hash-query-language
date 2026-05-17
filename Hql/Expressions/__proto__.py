from Hql.Parser.Object import ParseObject

# An expression is any grouping of other expressions
# Typically children of an operation, an expression can also contain operators itself
# Such as a subsearch, which is an expression, and contains operators
# All other expressions are children of this one
class Expression(ParseObject):
    def __init__(self)-> None:
        ParseObject.__init__(self)
        self.escaped     = False
        self.literal     = False
        self.logic       = False
        self.value       = None
        self.tabular     = False
        self.requires_lh = False

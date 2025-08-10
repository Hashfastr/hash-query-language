from Hql.Expressions.Logic import BinaryLogic


class SigmaSelection():
    def __init__(self, name:str, selection:dict):
        self.name = name
        self.selection = selection
        self.fields = dict()

    def process_fields(self):
        for i in self.selection:
            self.fields[i] = self.process_field(i, self.selection[i])
        return self.build_selection()

    def build_selection(self):
        ...

    def process_field(self, name:str, field):
        import Hql.Expressions as Expr
        fl = isinstance(field, list)

        name = name.split('|')[0]
        modifiers = name.split('|')[1:]

        lh = Expr.NamedReference(name)

        if 'contains' in modifiers:
            Expr.Contains()



        if 'all' in modifiers:
            ...

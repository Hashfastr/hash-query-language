See @README.md for context.

The goal here is to update old code to use the new current methods as part of a large systemic rewrite.
Some code has been updated, some hasn't.

Each query operator in Hql is defined as a subclass of the Operator class shown in @Hql/Operators/Operator.py
Expressions as defined in @Hql/Expressions should be used and not have base values stripped from them.
For example Integer expressions should not be turned into python int types unless absolutely necessary.

@Hql/Operators/Count.py is an example of a rewritten Operator.
@Hql/Operators/Sort.py is an example of a non-rewritten Operator.

Typing was meant to become consistent, that is having a generic self.expr attribute that is typed to the broad Expression type.
Operators then narrow down on this as needed and provide their own types when accessed.
For example, @Hql/Operators/Take.py has self.expr as Integer.
My linter complains however, and I am using a semi-hacky method of properties and setters to get around the typing issues resulting from attempting to narrow an Optional['Expression'].

Ensure code is minimal and clean.
Code should be simple, auditable, and use existing data structures for this program.

Unless absolutely necessary only make edits to code in @Hql/Operators

If any design changes are to be made, ensure I am consulted before they are made.

# Plain errors
Errors I've found in the kusto grammar that either exist as a fuck you or a open source we don't care.

These could also be Canary Trap, a way to figure out who's using Microsoft developed code.
In this case grammar, which isn't code.

These are typically not in production, I assume their repos are split between internal and opensource.
I'm sure they're killing opensource which is why these have not been updated

## Summarize
Might get fixed here:
https://github.com/microsoft/Kusto-Query-Language/pull/159

This
```
summarizeOperatorByClause:
    BY Expressions+=namedExpression (',' Expressions+=namedExpression) (BinClause=summarizeOperatorLegacyBinClause)?;
```

Should be this
```
summarizeOperatorByClause:
    BY Expressions+=namedExpression (',' Expressions+=namedExpression)* (BinClause=summarizeOperatorLegacyBinClause)?;
```

Otherwise it is required at all times by grammar to have exactly two by expressions.
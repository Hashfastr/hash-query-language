# Cut Kusto features and other weird grammar
I'm unsure about the inner workings of Kusto's team over at M$, but there are some odd and weird choices in Kusto's grammar.
Below are some of the reasons why I've modified or tuned the grammar of Hql to be

1. More efficient
2. Actually correct

## Query Operator Parameters
This seems to be a common thing among *all* operator grammars.
They're all supposed to take parameters, but are rarely accepted.

```
countOperator:
    COUNT (Parameters+=relaxedQueryOperatorParameter)*;

// allows any identifier
relaxedQueryOperatorParameter:
    NameToken=(
          IDENTIFIER
        | BAGEXPANSION
        | BIN_LEGACY
        | CROSSCLUSTER__
        | CROSSDB__
        | DECODEBLOCKS
        | EXPANDOUTPUT
        | HINT_CONCURRENCY
        | HINT_DISTRIBUTION
        | HINT_MATERIALIZED
        | HINT_NUM_PARTITIONS
        | HINT_PASS_FILTERS
        | HINT_PASS_FILTERS_COLUMN
        | HINT_PROGRESSIVE_TOP
        | HINT_REMOTE
        | HINT_SUFFLEKEY
        | HINT_SPREAD
        | HINT_STRATEGY
        | ISFUZZY
        | ISFUZZY__
        | ID__
        | KIND
        | PACKEDCOLUMN__
        | SOURCECOLUMNINDEX__
        | WITH_ITEM_INDEX
        | WITH_MATCH_ID
        | WITH_STEP_NAME
        | WITHSOURCE
        | WITH_SOURCE
        | WITHNOSOURCE__
        )
    '=' (NameValue=identifierOrKeywordName | LiteralValue=literalExpression)
    ;
```

So then the following are syntactically valid:

```
// Not valid
| count key="value"

// This is literally impossible as it's over written by the actual comparator
// Aditionally ADX complains that the below is not valid as it needs a bool
| where key=value

// Also syntactically valid
| project key=1
```

`relaxedQueryOperatorParameter` is defined for every operator, but not used often.
Really weird, I'm not sure if there's a rare feature somewhere that allows one to add these params.
As far as I can tell you cannot

1. Create your own operators
2. Modify built in operators

The only thing you can do is create functions that can be used with summarize and the like.
Although these are not considered these parameters.

## Count
This is the defined grammar for the count operator.

```
countOperator:
    COUNT (Parameters+=relaxedQueryOperatorParameter)*;

countOperatorAsClause:
    AS Name=identifierName;
```

Supposedly there was supposed to be an `as` clause for count.
Official Kusto docs show that the syntax for count is just as follows:

```
| count
```

But the cut `as` clause would've probably worked like this:

```
| count as T1
```

Where T1 would've been a table given the counts.
Within the grammar this is a island non-terminal token, not used anywhere, and is not valid in ADX.

#### NOTE
Some time between me initially writing this and now they've implemented it.
The documentation has not been caught up but the as clause is now implemented.
It will rename the count field from 'Count' to whatever you'd like.
Unsure why this is really needed but whatever.

I assume since count is an alias to 

```
| summarize Count=count()
```

It's just changing the name assignment

### In Hql
I've reintroduced this as Hql works well with multiple tables.
I think it's helpful to have the option to not wipe everything and replace with counts.
When the `as` clause is used it puts all counts into the table referenced by `as`, as is usual in other uses of `as`.

## Take
This is the defined grammar for the count operator.

```
takeOperator:
    Keyword=(LIMIT | TAKE) (Parameters+=strictQueryOperatorParameter)* Expression=namedExpression;

namedExpression:
    (Name=namedExpressionNameClause)? Expression=unnamedExpression;

namedExpressionNameClause:
    (Name=identifierOrExtendedKeywordOrEscapedName | NameList=namedExpressionNameList) '=';  
```

I included the `namedExpression` non-terminals as well to show this.
The documented syntax for take is as follows:

```
| take INTEGER
// OR
| take 10
```

Although the above syntax shows that it currently accepts a namedExpression.
That is an expression with a variable assignment.
I believe this is an error, but it still works in Kusto.

```
| take variable=10
```

Is valid, however does nothing.
Verified in ADX, the above is semantically equivalent to:

```
| take 10
```

As I believe the result of the assignment is just used.
There's nothing this does, no column is created in the data, nothing is modified.
The `unnamedExpression` non-terminal would semantically do the same.

Oddly enough, some grammars defined by `unnamedExpression` make no sense and are not accepted by ADX.

```
| take 1 == 1
```

Is valid grammar, but is semantically invalid.

### In Hql
Not implemented, the `namedExpression` grammar is replaced with `unnamedExpression`.
Will be changed again when I optimize the grammar.

## Join
Valid kusto, but undocumented, shows that you can have a where clause instead of 'on'.
When you use it, it basically acts as a prefilter for the right-hand side.

```
| join kind=inner right where ham == 'a'

// Is the same as

| join kind=inner (right | where ham == 'a')
```

The real difference between the two is that you can actually use the on clause on the second one.

```
// invalid
| join kind=inner right where ham == 'a' on ham

// valid
| join kind=inner (right | where ham == 'a') on ham
```

So, I'm considering just nuking this, or just doing a where passthrough to the right compilerset.
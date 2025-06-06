# Casting functions
Basic functions used to cast a value to a Hql Type.
See the typing doc for specifics which types do and are what, e.g. Hql int is a Polars Int32.

All functions have the following basic syntax:

```
Dataset
| project int_as_str, int = toint(int_as_str)

// Pseudo
[
    {"int_as_str": "10", "int": 10},
    {"int_as_str": "15", "int": 15},
    {"int_as_str": "34", "int": 34},
    {"int_as_str": "29", "int": 29},
]
```

## toint()
Convert a field to a basic Hql int.

## toip4()
Converts an ip4 string into an Hql ip4 type.
While stored as a UInt32, it is converted back into a string upon display to the user.
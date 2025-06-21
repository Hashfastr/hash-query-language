let left = datatable (foo: int, bar: double, ham: string)
[
    1, 6.0, 'a',
    2, 7.0, 'b',
    3, 8.0, 'd'
];
let right = datatable (pork: string, apple: string)
[
    'a', 'x',
    'b', 'y',
    'c', 'z'
];
left
| join kind=fullouter right on $left.ham == $right.pork
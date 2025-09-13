let shapes = datatable (name: string, sideCount: int)
[
    "triangle", 3,
    "square", 4,
    "rectangle", 4,
    "pentagon", 5,
    "hexagon", 6,
    "heptagon", 7,
    "octagon", 8,
    "nonagon", 9,
    "decagon", 10
] as shapes;
let numberNames = datatable (sideCount: int, sideName: string)
[
    3, 'three',
    4, 'four',
    4, 'four',
    5, 'five',
    6, 'six',
    7, 'seven',
    8, 'eight',
    9, 'nine',
    10, 'ten'
] as names;
union shapes, numberNames
| rename shapes to bapes, names to crepes

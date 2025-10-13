let shapes = datatable (name: string, sideCount: int)
[
    "Triangle", 3,
    "square", 4,
    "rectangle", 4,
    "pentagon", 5,
    "hexagon", 6,
    "heptagon", 7,
    "octagon", 8,
    "nonagon", 9,
    "decagon", 10
];
let specialshape = 'triangle';
shapes
| take 5
| where name =~ specialshape
| where test.specialshape == 1

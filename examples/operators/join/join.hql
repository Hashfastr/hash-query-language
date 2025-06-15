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
];
let special_numbers = datatable (num: int)
[
    4,
    7,
    10
];
shapes
| join kind=rightouter special_numbers on $left.sideCount == $right.num
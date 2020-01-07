graph [
  label "random"
  node [
    id 0
    label "glycerate_3_phosphate"
  ]
  node [
    id 1
    label "beta;-alanine"
  ]
  node [
    id 2
    label "l-methionine"
  ]
  node [
    id 3
    label "succinate"
  ]
  node [
    id 4
    label "glucose"
  ]
  node [
    id 5
    label "threonate"
  ]
  node [
    id 6
    label "l-phenylalanine"
  ]
  node [
    id 7
    label "uracil"
  ]
  node [
    id 8
    label "galactose"
  ]
  node [
    id 9
    label "inositol"
  ]
  node [
    id 10
    label "l-arginine"
  ]
  node [
    id 11
    label "gdp-beta;-l-fucose"
  ]
  edge [
    source 1
    target 10
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 1
    target 6
    weight 1
  ]
  edge [
    source 2
    target 10
    weight 1
  ]
  edge [
    source 2
    target 6
    weight 1
  ]
  edge [
    source 4
    target 8
    weight 1
  ]
  edge [
    source 5
    target 11
    weight 1
  ]
  edge [
    source 6
    target 10
    weight 1
  ]
  edge [
    source 6
    target 11
    weight 1
  ]
  edge [
    source 6
    target 7
    weight 1
  ]
  edge [
    source 7
    target 11
    weight 1
  ]
]

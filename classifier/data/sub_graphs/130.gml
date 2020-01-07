graph [
  label "random"
  node [
    id 0
    label "succinate"
  ]
  node [
    id 1
    label "l-cysteine"
  ]
  node [
    id 2
    label "2-oxoglutarate"
  ]
  node [
    id 3
    label "l-lysine"
  ]
  node [
    id 4
    label "l-threonine"
  ]
  node [
    id 5
    label "phosphate"
  ]
  node [
    id 6
    label "l-aspartate"
  ]
  node [
    id 7
    label "l-glutamate"
  ]
  node [
    id 8
    label "l-methionine"
  ]
  edge [
    source 1
    target 8
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 3
    target 8
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
  edge [
    source 4
    target 8
    weight 1
  ]
  edge [
    source 5
    target 6
    weight 1
  ]
  edge [
    source 5
    target 7
    weight 1
  ]
  edge [
    source 6
    target 7
    weight 1
  ]
]

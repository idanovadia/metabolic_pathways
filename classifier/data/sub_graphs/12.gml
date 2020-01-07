graph [
  label "random"
  node [
    id 0
    label "l-methionine"
  ]
  node [
    id 1
    label "succinate"
  ]
  node [
    id 2
    label "l-cysteine"
  ]
  node [
    id 3
    label "2-oxoglutarate"
  ]
  node [
    id 4
    label "l-lysine"
  ]
  node [
    id 5
    label "l-threonine"
  ]
  node [
    id 6
    label "phosphate"
  ]
  node [
    id 7
    label "l-aspartate"
  ]
  node [
    id 8
    label "l-glutamate"
  ]
  node [
    id 9
    label "l-glutamine"
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 0
    target 4
    weight 1
  ]
  edge [
    source 0
    target 5
    weight 1
  ]
  edge [
    source 2
    target 5
    weight 1
  ]
  edge [
    source 4
    target 5
    weight 1
  ]
  edge [
    source 6
    target 7
    weight 1
  ]
  edge [
    source 6
    target 8
    weight 1
  ]
  edge [
    source 7
    target 8
    weight 1
  ]
]

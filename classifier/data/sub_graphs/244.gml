graph [
  label "random"
  node [
    id 0
    label "2-oxoglutarate"
  ]
  node [
    id 1
    label "l-lysine"
  ]
  node [
    id 2
    label "phosphate"
  ]
  node [
    id 3
    label "l-aspartate"
  ]
  node [
    id 4
    label "l-glutamate"
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
]

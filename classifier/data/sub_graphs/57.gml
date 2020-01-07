graph [
  label "random"
  node [
    id 0
    label "succinate"
  ]
  node [
    id 1
    label "2-oxoglutarate"
  ]
  node [
    id 2
    label "l-lysine"
  ]
  node [
    id 3
    label "phosphate"
  ]
  node [
    id 4
    label "l-aspartate"
  ]
  node [
    id 5
    label "l-glutamate"
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
  edge [
    source 4
    target 5
    weight 1
  ]
]

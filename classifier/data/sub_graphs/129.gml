graph [
  label "random"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "l-alanine"
  ]
  node [
    id 3
    label "l-lysine"
  ]
  node [
    id 4
    label "succinate"
  ]
  node [
    id 5
    label "2-oxoglutarate"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 2
    target 5
    weight 1
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
    target 5
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
  edge [
    source 4
    target 5
    weight 1
  ]
]

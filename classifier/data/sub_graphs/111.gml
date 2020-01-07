graph [
  label "random"
  node [
    id 0
    label "fumarate"
  ]
  node [
    id 1
    label "putrescine"
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
    label "phosphate"
  ]
  node [
    id 5
    label "l-arginine"
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
    label "l-glutamine"
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
  edge [
    source 4
    target 6
    weight 1
  ]
  edge [
    source 4
    target 7
    weight 1
  ]
  edge [
    source 6
    target 7
    weight 1
  ]
]

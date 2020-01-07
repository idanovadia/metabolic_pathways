graph [
  label "random"
  node [
    id 0
    label "fumarate"
  ]
  node [
    id 1
    label "2-oxoglutarate"
  ]
  node [
    id 2
    label "phosphate"
  ]
  node [
    id 3
    label "l-arginine"
  ]
  node [
    id 4
    label "l-aspartate"
  ]
  node [
    id 5
    label "l-glutamate"
  ]
  node [
    id 6
    label "l-glutamine"
  ]
  edge [
    source 2
    target 4
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
]

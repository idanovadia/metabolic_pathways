graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "2-oxoglutarate"
  ]
  node [
    id 1
    label "l-arginine"
  ]
  node [
    id 2
    label "l-glutamate"
  ]
  node [
    id 3
    label "fumarate"
  ]
  node [
    id 4
    label "l-glutamine"
  ]
  node [
    id 5
    label "phosphate"
  ]
  node [
    id 6
    label "l-aspartate"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 2
    target 6
    weight 1
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
    target 6
    weight 1
  ]
  edge [
    source 4
    target 5
    weight 1
  ]
  edge [
    source 5
    target 6
    weight 1
  ]
]

graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "fumarate"
  ]
  node [
    id 2
    label "l-glutamate"
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
    label "2-oxoglutarate"
  ]
  node [
    id 6
    label "l-glutamine"
  ]
  edge [
    source 0
    target 3
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 4
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 0
    target 6
  ]
  edge [
    source 1
    target 3
  ]
  edge [
    source 2
    target 4
  ]
  edge [
    source 2
    target 6
  ]
  edge [
    source 4
    target 6
  ]
]

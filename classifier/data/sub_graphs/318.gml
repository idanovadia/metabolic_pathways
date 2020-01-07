graph [
  label "random"
  node [
    id 0
    label "l-homoserine"
  ]
  node [
    id 1
    label "2-oxoglutarate"
  ]
  node [
    id 2
    label "l-threonine"
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
    source 0
    target 2
    weight 1
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

graph [
  label "random"
  node [
    id 0
    label "l-isoleucine"
  ]
  node [
    id 1
    label "phosphate"
  ]
  node [
    id 2
    label "l-glutamate"
  ]
  node [
    id 3
    label "l-threonine"
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
    label "l-homoserine"
  ]
  edge [
    source 0
    target 5
    weight 1
  ]
  edge [
    source 0
    target 6
    weight 1
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 1
    target 2
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
    target 6
    weight 1
  ]
  edge [
    source 5
    target 6
    weight 1
  ]
]

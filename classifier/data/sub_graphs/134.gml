graph [
  label "random"
  node [
    id 0
    label "glycine"
  ]
  node [
    id 1
    label "2-oxoglutarate"
  ]
  node [
    id 2
    label "l-isoleucine"
  ]
  node [
    id 3
    label "l-threonine"
  ]
  node [
    id 4
    label "phosphate"
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
    source 0
    target 3
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
  edge [
    source 4
    target 5
    weight 1
  ]
]

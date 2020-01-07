graph [
  label "random"
  node [
    id 0
    label "l-isoleucine"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "l-leucine"
  ]
  node [
    id 3
    label "l-valine"
  ]
  node [
    id 4
    label "2-oxoglutarate"
  ]
  node [
    id 5
    label "l-threonine"
  ]
  edge [
    source 0
    target 4
    weight 1
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 0
    target 5
    weight 1
  ]
  edge [
    source 0
    target 3
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
    source 2
    target 3
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

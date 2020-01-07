graph [
  label "random"
  node [
    id 0
    label "l-isoleucine"
  ]
  node [
    id 1
    label "l-leucine"
  ]
  node [
    id 2
    label "l-valine"
  ]
  node [
    id 3
    label "l-phenylalanine"
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
    source 0
    target 2
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
]

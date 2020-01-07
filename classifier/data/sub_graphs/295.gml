graph [
  label "random"
  node [
    id 0
    label "l-glutamine"
  ]
  node [
    id 1
    label "l-isoleucine"
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
    label "l-phenylalanine"
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 1
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
    target 3
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
]

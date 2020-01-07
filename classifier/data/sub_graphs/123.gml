graph [
  label "random"
  node [
    id 0
    label "l-leucine"
  ]
  node [
    id 1
    label "glucose"
  ]
  node [
    id 2
    label "l-phenylalanine"
  ]
  node [
    id 3
    label "l-alanine"
  ]
  node [
    id 4
    label "l-valine"
  ]
  node [
    id 5
    label "l-aspartate"
  ]
  node [
    id 6
    label "l-glutamate"
  ]
  node [
    id 7
    label "l-glutamine"
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
    source 0
    target 4
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
  edge [
    source 5
    target 6
    weight 1
  ]
]

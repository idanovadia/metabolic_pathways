graph [
  label "random"
  type "trainset"
  node [
    id 0
    label "(s)-malate"
  ]
  node [
    id 1
    label "l-valine"
  ]
  node [
    id 2
    label "l-lysine"
  ]
  node [
    id 3
    label "phosphate"
  ]
  node [
    id 4
    label "l-aspartate"
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
]

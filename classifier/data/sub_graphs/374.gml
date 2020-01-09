graph [
  label "random"
  type "trainset"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "l-aspartate"
  ]
  node [
    id 2
    label "l-valine"
  ]
  node [
    id 3
    label "(s)-malate"
  ]
  node [
    id 4
    label "l-lysine"
  ]
  edge [
    source 0
    target 1
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

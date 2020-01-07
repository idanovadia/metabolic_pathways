graph [
  label "random"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "(s)-malate"
  ]
  node [
    id 2
    label "l-lysine"
  ]
  node [
    id 3
    label "l-valine"
  ]
  node [
    id 4
    label "l-aspartate"
  ]
  edge [
    source 0
    target 4
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
]

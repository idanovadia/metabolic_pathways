graph [
  label "random"
  type "trainset"
  node [
    id 0
    label "l-lysine"
  ]
  node [
    id 1
    label "l-alanine"
  ]
  node [
    id 2
    label "l-arginine"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
]
graph [
  label "random"
  type "trainset"
  name "380.gml"
  node [
    id 0
    label "maltose"
  ]
  node [
    id 1
    label "(s)-malate"
  ]
  node [
    id 2
    label "l-isoleucine"
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
]

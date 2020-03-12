graph [
  label "random"
  type "trainset"
  name "403.gml"
  node [
    id 0
    label "l-valine"
  ]
  node [
    id 1
    label "glucose_6_phosphate"
  ]
  node [
    id 2
    label "l-isoleucine"
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

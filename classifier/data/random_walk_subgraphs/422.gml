graph [
  label "random"
  type "trainset"
  name "422.gml"
  node [
    id 0
    label "l-glutamate"
  ]
  node [
    id 1
    label "d-threo-isocitrate"
  ]
  node [
    id 2
    label "glucose"
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

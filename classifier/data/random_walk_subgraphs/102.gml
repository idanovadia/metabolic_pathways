graph [
  label "negative"
  type "trainset"
  name "102.gml"
  node [
    id 0
    label "l-tryptophan"
  ]
  node [
    id 1
    label "l-alanine"
  ]
  node [
    id 2
    label "2-oxoglutarate"
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

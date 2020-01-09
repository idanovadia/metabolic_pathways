graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "glucose"
  ]
  node [
    id 1
    label "2-oxoglutarate"
  ]
  node [
    id 2
    label "l-phenylalanine"
  ]
  node [
    id 3
    label "succinate"
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

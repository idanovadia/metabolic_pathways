graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "shikimate"
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
    label "l-glutamate"
  ]
  node [
    id 4
    label "phosphate"
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
  edge [
    source 3
    target 4
    weight 1
  ]
]

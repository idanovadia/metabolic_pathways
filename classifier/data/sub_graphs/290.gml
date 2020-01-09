graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "l-tyrosine"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "2-oxoglutarate"
  ]
  node [
    id 3
    label "l-phenylalanine"
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
]

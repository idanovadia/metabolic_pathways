graph [
  label "testset"
  type "classifier/data/labeled_data/2001"
  node [
    id 0
    label "l-glutamate"
  ]
  node [
    id 1
    label "l-tryptophan"
  ]
  node [
    id 2
    label "l-alanine"
  ]
  node [
    id 3
    label "2-oxoglutarate"
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

graph [
  label "testset"
  type "classifier/data/labeled_data/2001"
  node [
    id 0
    label "l-tryptophan"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "glucose"
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 1
    target 2
  ]
]

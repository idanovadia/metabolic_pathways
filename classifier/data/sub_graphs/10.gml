graph [
  label "testset"
  type "classifier/data/labeled_data/2001"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "beta;-alanine"
  ]
  node [
    id 2
    label "l-glutamate"
  ]
  node [
    id 3
    label "l-cysteine"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 3
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 1
    target 3
  ]
]

graph [
  label "testset"
  type "classifier/data/labeled_data/2001"
  node [
    id 0
    label "l-glutamate"
  ]
  node [
    id 1
    label "beta;-alanine"
  ]
  node [
    id 2
    label "l-cysteine"
  ]
  node [
    id 3
    label "phosphate"
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
]

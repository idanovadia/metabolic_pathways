graph [
  label "testset"
  type "classifier/data/labeled_data/2001"
  node [
    id 0
    label "l-asparagine"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "l-glutamine"
  ]
  node [
    id 3
    label "2-oxoglutarate"
  ]
  node [
    id 4
    label "l-aspartate"
  ]
  edge [
    source 0
    target 3
  ]
  edge [
    source 0
    target 4
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 1
    target 4
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 2
    target 4
  ]
  edge [
    source 3
    target 4
  ]
]

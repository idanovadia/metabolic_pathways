graph [
  label "testset"
  type "classifier/data/labeled_data/2001"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "fumarate"
  ]
  node [
    id 2
    label "l-glutamate"
  ]
  node [
    id 3
    label "l-aspartate"
  ]
  node [
    id 4
    label "l-glutamine"
  ]
  node [
    id 5
    label "glycine"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 5
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
    source 0
    target 4
  ]
  edge [
    source 1
    target 5
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 2
    target 4
  ]
  edge [
    source 3
    target 5
  ]
  edge [
    source 3
    target 4
  ]
]

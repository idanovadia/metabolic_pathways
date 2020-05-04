graph [
  label "testset"
  type "classifier/data/labeled_data/2001"
  node [
    id 0
    label "l-glutamate"
  ]
  node [
    id 1
    label "l-aspartate"
  ]
  node [
    id 2
    label "phosphate"
  ]
  node [
    id 3
    label "l-glutamine"
  ]
  node [
    id 4
    label "glycine"
  ]
  node [
    id 5
    label "fumarate"
  ]
  edge [
    source 0
    target 5
  ]
  edge [
    source 0
    target 4
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
    source 0
    target 3
  ]
  edge [
    source 1
    target 5
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
    source 1
    target 3
  ]
  edge [
    source 2
    target 5
  ]
  edge [
    source 2
    target 4
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 3
    target 4
  ]
  edge [
    source 4
    target 5
  ]
]

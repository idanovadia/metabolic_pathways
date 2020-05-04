graph [
  label "testset"
  type "classifier/data/labeled_data/2001"
  node [
    id 0
    label "2-oxoglutarate"
  ]
  node [
    id 1
    label "l-arginine"
  ]
  node [
    id 2
    label "succinate"
  ]
  node [
    id 3
    label "l-glutamate"
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
    target 2
  ]
  edge [
    source 1
    target 3
  ]
  edge [
    source 2
    target 3
  ]
]

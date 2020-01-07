graph [
  label "random"
  node [
    id 0
    label "l-alanine"
  ]
  node [
    id 1
    label "2-oxoglutarate"
  ]
  node [
    id 2
    label "l-glutamate"
  ]
  node [
    id 3
    label "l-phenylalanine"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
]

graph [
  label "random"
  node [
    id 0
    label "benzoate"
  ]
  node [
    id 1
    label "succinate"
  ]
  node [
    id 2
    label "l-phenylalanine"
  ]
  node [
    id 3
    label "2-oxoglutarate"
  ]
  node [
    id 4
    label "phosphate"
  ]
  node [
    id 5
    label "fumarate"
  ]
  node [
    id 6
    label "l-glutamate"
  ]
  edge [
    source 0
    target 5
    weight 1
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 4
    target 6
    weight 1
  ]
]

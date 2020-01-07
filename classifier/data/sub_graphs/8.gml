graph [
  label "random"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "fumarate"
  ]
  node [
    id 3
    label "benzoate"
  ]
  node [
    id 4
    label "succinate"
  ]
  node [
    id 5
    label "l-phenylalanine"
  ]
  node [
    id 6
    label "2-oxoglutarate"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 2
    target 6
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
  edge [
    source 2
    target 5
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
  edge [
    source 3
    target 6
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
  edge [
    source 4
    target 6
    weight 1
  ]
  edge [
    source 4
    target 5
    weight 1
  ]
  edge [
    source 5
    target 6
    weight 1
  ]
]

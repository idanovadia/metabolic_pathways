graph [
  label "random"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "succinate"
  ]
  node [
    id 2
    label "2-oxoglutarate"
  ]
  node [
    id 3
    label "l-serine"
  ]
  node [
    id 4
    label "l-alanine"
  ]
  node [
    id 5
    label "(s)-malate"
  ]
  node [
    id 6
    label "fumarate"
  ]
  node [
    id 7
    label "l-aspartate"
  ]
  node [
    id 8
    label "l-glutamate"
  ]
  edge [
    source 0
    target 7
    weight 1
  ]
  edge [
    source 0
    target 8
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
  edge [
    source 7
    target 8
    weight 1
  ]
]

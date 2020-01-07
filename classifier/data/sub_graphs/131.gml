graph [
  label "random"
  node [
    id 0
    label "succinate"
  ]
  node [
    id 1
    label "l-cysteine"
  ]
  node [
    id 2
    label "2-oxoglutarate"
  ]
  node [
    id 3
    label "phosphate"
  ]
  node [
    id 4
    label "l-aspartate"
  ]
  node [
    id 5
    label "l-glutamate"
  ]
  node [
    id 6
    label "l-methionine"
  ]
  edge [
    source 1
    target 6
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
  edge [
    source 4
    target 5
    weight 1
  ]
]

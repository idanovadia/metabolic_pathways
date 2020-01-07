graph [
  label "random"
  node [
    id 0
    label "l-tryptophan"
  ]
  node [
    id 1
    label "phosphate"
  ]
  node [
    id 2
    label "2-oxoglutarate"
  ]
  node [
    id 3
    label "succinate"
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
]

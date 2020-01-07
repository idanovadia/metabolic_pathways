graph [
  label "random"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "glycine"
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
    source 1
    target 2
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
]

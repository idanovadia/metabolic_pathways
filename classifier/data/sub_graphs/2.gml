graph [
  label "random"
  node [
    id 0
    label "l-leucine"
  ]
  node [
    id 1
    label "2-oxoglutarate"
  ]
  node [
    id 2
    label "succinate"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
]

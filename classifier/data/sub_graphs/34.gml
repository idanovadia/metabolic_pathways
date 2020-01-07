graph [
  label "random"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "(s)-malate"
  ]
  node [
    id 2
    label "l-serine"
  ]
  node [
    id 3
    label "glycine"
  ]
  node [
    id 4
    label "d-glycerate"
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
]

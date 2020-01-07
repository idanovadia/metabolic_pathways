graph [
  label "random"
  node [
    id 0
    label "glycine"
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
    label "phosphate"
  ]
  node [
    id 4
    label "d-glycerate"
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

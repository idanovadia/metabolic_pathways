graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "d-glycerate"
  ]
  node [
    id 1
    label "(s)-malate"
  ]
  node [
    id 2
    label "glycine"
  ]
  node [
    id 3
    label "phosphate"
  ]
  node [
    id 4
    label "l-serine"
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 0
    target 4
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
]

graph [
  label "negative"
  type "trainset"
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
    label "l-serine"
  ]
  node [
    id 3
    label "d-glycerate"
  ]
  node [
    id 4
    label "(s)-malate"
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
]

graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "cis-aconitate"
  ]
  node [
    id 1
    label "2-oxoglutarate"
  ]
  node [
    id 2
    label "succinate"
  ]
  node [
    id 3
    label "(s)-malate"
  ]
  node [
    id 4
    label "fumarate"
  ]
  node [
    id 5
    label "d-threo-isocitrate"
  ]
  node [
    id 6
    label "phosphate"
  ]
  node [
    id 7
    label "citrate"
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
    source 0
    target 3
    weight 1
  ]
  edge [
    source 0
    target 2
    weight 1
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
  edge [
    source 5
    target 7
    weight 1
  ]
  edge [
    source 5
    target 6
    weight 1
  ]
  edge [
    source 6
    target 7
    weight 1
  ]
]
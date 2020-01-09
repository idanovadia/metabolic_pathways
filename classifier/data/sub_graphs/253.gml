graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "cis-aconitate"
  ]
  node [
    id 1
    label "succinate"
  ]
  node [
    id 2
    label "d-threo-isocitrate"
  ]
  node [
    id 3
    label "(s)-malate"
  ]
  node [
    id 4
    label "citrate"
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
]

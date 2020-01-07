graph [
  label "random"
  node [
    id 0
    label "d-threo-isocitrate"
  ]
  node [
    id 1
    label "(s)-malate"
  ]
  node [
    id 2
    label "cis-aconitate"
  ]
  node [
    id 3
    label "succinate"
  ]
  node [
    id 4
    label "citrate"
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
    target 3
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
]

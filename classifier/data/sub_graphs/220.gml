graph [
  label "random"
  node [
    id 0
    label "succinate"
  ]
  node [
    id 1
    label "citrate"
  ]
  node [
    id 2
    label "cis-aconitate"
  ]
  node [
    id 3
    label "(s)-malate"
  ]
  node [
    id 4
    label "d-threo-isocitrate"
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
]

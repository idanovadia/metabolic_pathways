graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "citrate"
  ]
  node [
    id 1
    label "cis-aconitate"
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
    label "succinate"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 3
  ]
  edge [
    source 0
    target 4
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 1
    target 3
  ]
  edge [
    source 1
    target 4
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 3
    target 4
  ]
]

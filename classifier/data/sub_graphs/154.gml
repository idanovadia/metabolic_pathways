graph [
  label "random"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "d-threo-isocitrate"
  ]
  node [
    id 2
    label "l-glutamate"
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
    label "succinate"
  ]
  node [
    id 6
    label "citrate"
  ]
  node [
    id 7
    label "2-oxoglutarate"
  ]
  edge [
    source 0
    target 6
    weight 1
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
    source 1
    target 6
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 2
    target 6
    weight 1
  ]
  edge [
    source 3
    target 7
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
  edge [
    source 4
    target 7
    weight 1
  ]
  edge [
    source 4
    target 5
    weight 1
  ]
  edge [
    source 5
    target 7
    weight 1
  ]
]

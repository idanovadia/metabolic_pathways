graph [
  label "random"
  node [
    id 0
    label "phosphate"
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
    label "2-oxoglutarate"
  ]
  node [
    id 4
    label "citrate"
  ]
  node [
    id 5
    label "(s)-malate"
  ]
  node [
    id 6
    label "fumarate"
  ]
  node [
    id 7
    label "l-glutamate"
  ]
  edge [
    source 0
    target 4
    weight 1
  ]
  edge [
    source 0
    target 7
    weight 1
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
]

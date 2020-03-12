graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "2-oxoglutarate"
  ]
  node [
    id 1
    label "succinate"
  ]
  node [
    id 2
    label "(s)-malate"
  ]
  node [
    id 3
    label "l-glutamate"
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
    label "l-aspartate"
  ]
  node [
    id 8
    label "citrate"
  ]
  edge [
    source 0
    target 4
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
    target 4
    weight 1
  ]
  edge [
    source 3
    target 7
    weight 1
  ]
  edge [
    source 3
    target 8
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
  edge [
    source 3
    target 6
    weight 1
  ]
  edge [
    source 5
    target 7
    weight 1
  ]
  edge [
    source 5
    target 8
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
  edge [
    source 6
    target 8
    weight 1
  ]
  edge [
    source 7
    target 8
    weight 1
  ]
]

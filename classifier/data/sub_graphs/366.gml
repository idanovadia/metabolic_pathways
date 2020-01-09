graph [
  label "random"
  type "trainset"
  node [
    id 0
    label "(s)-malate"
  ]
  node [
    id 1
    label "d-gluconate"
  ]
  node [
    id 2
    label "gdp-beta;-l-fucose"
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
    target 2
    weight 1
  ]
]

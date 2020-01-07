graph [
  label "random"
  node [
    id 0
    label "erythritol"
  ]
  node [
    id 1
    label "succinate"
  ]
  node [
    id 2
    label "l-cysteine"
  ]
  node [
    id 3
    label "glucose"
  ]
  node [
    id 4
    label "l-phenylalanine"
  ]
  node [
    id 5
    label "2-oxoglutarate"
  ]
  node [
    id 6
    label "shikimate"
  ]
  node [
    id 7
    label "gdp-beta;-l-fucose"
  ]
  node [
    id 8
    label "d-glycerate"
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 0
    target 7
    weight 1
  ]
  edge [
    source 0
    target 8
    weight 1
  ]
  edge [
    source 0
    target 4
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
  edge [
    source 4
    target 7
    weight 1
  ]
]

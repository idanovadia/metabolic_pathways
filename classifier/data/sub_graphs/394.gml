graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "gdp-beta;-l-fucose"
  ]
  node [
    id 1
    label "l-phenylalanine"
  ]
  node [
    id 2
    label "shikimate"
  ]
  node [
    id 3
    label "succinate"
  ]
  node [
    id 4
    label "glucose"
  ]
  node [
    id 5
    label "erythritol"
  ]
  node [
    id 6
    label "d-glycerate"
  ]
  node [
    id 7
    label "2-oxoglutarate"
  ]
  node [
    id 8
    label "l-cysteine"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 5
  ]
  edge [
    source 1
    target 8
  ]
  edge [
    source 1
    target 5
  ]
  edge [
    source 5
    target 8
  ]
  edge [
    source 5
    target 6
  ]
]

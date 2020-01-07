graph [
  label "random"
  node [
    id 0
    label "benzoate"
  ]
  node [
    id 1
    label "alpha;-tocopherol"
  ]
  node [
    id 2
    label "succinate"
  ]
  node [
    id 3
    label "d-gluconate"
  ]
  node [
    id 4
    label "threonate"
  ]
  node [
    id 5
    label "l-isoleucine"
  ]
  node [
    id 6
    label "gdp-beta;-l-fucose"
  ]
  node [
    id 7
    label "d-glycerate"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 0
    target 6
    weight 1
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 4
    target 6
    weight 1
  ]
  edge [
    source 4
    target 7
    weight 1
  ]
]

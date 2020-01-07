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
    label "d-gluconate"
  ]
  node [
    id 3
    label "l-tyrosine"
  ]
  node [
    id 4
    label "l-isoleucine"
  ]
  node [
    id 5
    label "inositol"
  ]
  node [
    id 6
    label "d-threo-isocitrate"
  ]
  node [
    id 7
    label "maltitol"
  ]
  node [
    id 8
    label "l-methionine"
  ]
  edge [
    source 0
    target 6
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
  edge [
    source 3
    target 8
    weight 1
  ]
  edge [
    source 4
    target 8
    weight 1
  ]
]

graph [
  label "random"
  node [
    id 0
    label "l-isoleucine"
  ]
  node [
    id 1
    label "maltose"
  ]
  node [
    id 2
    label "(s)-malate"
  ]
  node [
    id 3
    label "uracil"
  ]
  node [
    id 4
    label "galactose"
  ]
  node [
    id 5
    label "citrate"
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
    source 0
    target 3
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
  edge [
    source 4
    target 5
    weight 1
  ]
]

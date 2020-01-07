graph [
  label "random"
  node [
    id 0
    label "l-asparagine"
  ]
  node [
    id 1
    label "(s)-malate"
  ]
  node [
    id 2
    label "alpha;,alpha;-trehalose"
  ]
  node [
    id 3
    label "inositol"
  ]
  node [
    id 4
    label "citrate"
  ]
  node [
    id 5
    label "udp-alpha;-d-galacturonate"
  ]
  edge [
    source 0
    target 5
    weight 1
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 1
    target 5
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 2
    target 5
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
]

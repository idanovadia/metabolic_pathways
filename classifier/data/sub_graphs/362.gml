graph [
  label "random"
  node [
    id 0
    label "glucose"
  ]
  node [
    id 1
    label "2-oxoglutarate"
  ]
  node [
    id 2
    label "(s)-malate"
  ]
  node [
    id 3
    label "l-isoleucine"
  ]
  node [
    id 4
    label "udp-alpha;-d-galacturonate"
  ]
  node [
    id 5
    label "alpha;,alpha;-trehalose"
  ]
  node [
    id 6
    label "inositol"
  ]
  node [
    id 7
    label "l-asparagine"
  ]
  node [
    id 8
    label "d-glycerate"
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
  edge [
    source 2
    target 5
    weight 1
  ]
  edge [
    source 3
    target 7
    weight 1
  ]
  edge [
    source 4
    target 5
    weight 1
  ]
]

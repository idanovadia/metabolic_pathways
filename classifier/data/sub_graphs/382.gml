graph [
  label "negative"
  type "trainset"
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
    label "inositol"
  ]
  node [
    id 3
    label "udp-alpha;-d-galacturonate"
  ]
  node [
    id 4
    label "alpha;,alpha;-trehalose"
  ]
  node [
    id 5
    label "citrate"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 1
    target 3
  ]
  edge [
    source 1
    target 4
  ]
  edge [
    source 3
    target 4
  ]
]

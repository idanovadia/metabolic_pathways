graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "glucose"
  ]
  node [
    id 1
    label "phosphate"
  ]
  node [
    id 2
    label "l-ascorbate"
  ]
  node [
    id 3
    label "udp-alpha;-d-galacturonate"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
]
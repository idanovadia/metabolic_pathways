graph [
  label "random"
  type "trainset"
  node [
    id 0
    label "alpha;-tocopherol"
  ]
  node [
    id 1
    label "benzoate"
  ]
  node [
    id 2
    label "fructose"
  ]
  node [
    id 3
    label "udp-alpha;-d-galacturonate"
  ]
  node [
    id 4
    label "l-serine"
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
    source 0
    target 4
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
]

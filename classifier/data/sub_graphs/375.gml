graph [
  label "random"
  type "trainset"
  node [
    id 0
    label "l-serine"
  ]
  node [
    id 1
    label "alpha;-tocopherol"
  ]
  node [
    id 2
    label "benzoate"
  ]
  node [
    id 3
    label "fructose"
  ]
  node [
    id 4
    label "udp-alpha;-d-galacturonate"
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
    source 0
    target 4
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
]

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
    label "l-serine"
  ]
  node [
    id 3
    label "udp-alpha;-d-galacturonate"
  ]
  node [
    id 4
    label "fructose"
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
    target 2
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
]

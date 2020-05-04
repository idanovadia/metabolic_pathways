graph [
  label "negative"
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
    label "fructose"
  ]
  node [
    id 3
    label "benzoate"
  ]
  node [
    id 4
    label "udp-alpha;-d-galacturonate"
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

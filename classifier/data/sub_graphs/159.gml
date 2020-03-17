graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "2-oxoglutarate"
  ]
  node [
    id 1
    label "succinate"
  ]
  node [
    id 2
    label "putrescine"
  ]
  node [
    id 3
    label "l-arginine"
  ]
  node [
    id 4
    label "l-glutamate"
  ]
  node [
    id 5
    label "phosphate"
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
    source 0
    target 1
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
    target 3
    weight 1
  ]
  edge [
    source 4
    target 5
    weight 1
  ]
]

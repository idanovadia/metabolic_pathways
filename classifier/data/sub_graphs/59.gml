graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "l-arginine"
  ]
  node [
    id 2
    label "succinate"
  ]
  node [
    id 3
    label "2-oxoglutarate"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 1
    target 2
  ]
]

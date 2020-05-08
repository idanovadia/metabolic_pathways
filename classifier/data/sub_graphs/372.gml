graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "l-glutamate"
  ]
  node [
    id 1
    label "(s)-malate"
  ]
  node [
    id 2
    label "glycerate_3_phosphate"
  ]
  node [
    id 3
    label "2-oxoglutarate"
  ]
  node [
    id 4
    label "l-isoleucine"
  ]
  edge [
    source 1
    target 4
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 2
    target 4
  ]
]

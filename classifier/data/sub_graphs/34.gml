graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "glycine"
  ]
  node [
    id 1
    label "2-oxoglutarate"
  ]
  node [
    id 2
    label "phosphate"
  ]
  node [
    id 3
    label "succinate"
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
    source 1
    target 3
    weight 1
  ]
]

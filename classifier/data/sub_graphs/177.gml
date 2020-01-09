graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "2-oxoglutarate"
  ]
  node [
    id 1
    label "phosphate"
  ]
  node [
    id 2
    label "putrescine"
  ]
  node [
    id 3
    label "l-aspartate"
  ]
  node [
    id 4
    label "l-glutamate"
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
    target 4
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
]

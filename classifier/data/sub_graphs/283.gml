graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "2-oxoglutarate"
  ]
  node [
    id 1
    label "putrescine"
  ]
  node [
    id 2
    label "l-glutamine"
  ]
  node [
    id 3
    label "phosphate"
  ]
  node [
    id 4
    label "l-methionine"
  ]
  edge [
    source 0
    target 4
    weight 1
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
]

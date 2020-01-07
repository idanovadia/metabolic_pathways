graph [
  label "random"
  node [
    id 0
    label "l-glutamine"
  ]
  node [
    id 1
    label "phosphate"
  ]
  node [
    id 2
    label "l-methionine"
  ]
  node [
    id 3
    label "putrescine"
  ]
  node [
    id 4
    label "2-oxoglutarate"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
]

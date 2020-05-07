graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "l-methionine"
  ]
  node [
    id 2
    label "putrescine"
  ]
  node [
    id 3
    label "2-oxoglutarate"
  ]
  node [
    id 4
    label "l-glutamine"
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
    source 0
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

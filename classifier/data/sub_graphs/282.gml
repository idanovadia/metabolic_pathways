graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "2-oxoglutarate"
  ]
  node [
    id 1
    label "l-glutamine"
  ]
  node [
    id 2
    label "l-methionine"
  ]
  node [
    id 3
    label "phosphate"
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 0
    target 3
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 1
    target 3
  ]
  edge [
    source 2
    target 3
  ]
]

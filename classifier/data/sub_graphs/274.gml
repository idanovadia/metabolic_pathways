graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "l-leucine"
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
    label "l-glutamate"
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 2
    target 3
  ]
]

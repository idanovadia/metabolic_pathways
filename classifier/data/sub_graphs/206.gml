graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "2-oxoglutarate"
  ]
  node [
    id 2
    label "l-glutamate"
  ]
  node [
    id 3
    label "l-glutamine"
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
    source 2
    target 3
  ]
]

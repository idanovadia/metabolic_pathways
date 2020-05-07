graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "d-glycerate"
  ]
  node [
    id 3
    label "l-serine"
  ]
  node [
    id 4
    label "2-oxoglutarate"
  ]
  node [
    id 5
    label "glycine"
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 0
    target 5
  ]
  edge [
    source 0
    target 3
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 2
    target 5
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 3
    target 5
  ]
]

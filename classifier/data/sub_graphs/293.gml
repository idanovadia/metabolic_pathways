graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "d-glycerate"
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
    label "glycine"
  ]
  node [
    id 4
    label "phosphate"
  ]
  node [
    id 5
    label "l-serine"
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
    source 0
    target 5
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 1
    target 5
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
]

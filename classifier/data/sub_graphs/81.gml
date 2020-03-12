graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "2-oxoglutarate"
  ]
  node [
    id 1
    label "succinate"
  ]
  node [
    id 2
    label "l-glutamate"
  ]
  node [
    id 3
    label "l-glutamine"
  ]
  node [
    id 4
    label "phosphate"
  ]
  node [
    id 5
    label "glucose"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 2
    target 5
    weight 1
  ]
  edge [
    source 2
    target 3
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
  edge [
    source 3
    target 4
    weight 1
  ]
  edge [
    source 4
    target 5
    weight 1
  ]
]

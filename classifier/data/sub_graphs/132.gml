graph [
  label "random"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "l-cysteine"
  ]
  node [
    id 2
    label "l-glutamate"
  ]
  node [
    id 3
    label "l-serine"
  ]
  node [
    id 4
    label "l-methionine"
  ]
  node [
    id 5
    label "2-oxoglutarate"
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 1
    target 5
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 1
    target 3
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

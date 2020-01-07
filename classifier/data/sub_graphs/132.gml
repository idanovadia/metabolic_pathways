graph [
  label "random"
  node [
    id 0
    label "l-cysteine"
  ]
  node [
    id 1
    label "2-oxoglutarate"
  ]
  node [
    id 2
    label "l-serine"
  ]
  node [
    id 3
    label "phosphate"
  ]
  node [
    id 4
    label "l-glutamate"
  ]
  node [
    id 5
    label "l-methionine"
  ]
  edge [
    source 0
    target 5
    weight 1
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 2
    target 5
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
]

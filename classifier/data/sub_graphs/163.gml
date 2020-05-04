graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "l-methionine"
  ]
  node [
    id 1
    label "l-threonine"
  ]
  node [
    id 2
    label "l-glutamate"
  ]
  node [
    id 3
    label "succinate"
  ]
  node [
    id 4
    label "l-lysine"
  ]
  node [
    id 5
    label "phosphate"
  ]
  node [
    id 6
    label "l-aspartate"
  ]
  node [
    id 7
    label "2-oxoglutarate"
  ]
  node [
    id 8
    label "l-cysteine"
  ]
  edge [
    source 0
    target 8
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 4
  ]
  edge [
    source 1
    target 8
  ]
  edge [
    source 1
    target 4
  ]
  edge [
    source 4
    target 8
  ]
]

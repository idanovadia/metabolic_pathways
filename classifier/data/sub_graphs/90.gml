graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "l-glutamate"
  ]
  node [
    id 1
    label "l-lysine"
  ]
  node [
    id 2
    label "phosphate"
  ]
  node [
    id 3
    label "succinate"
  ]
  node [
    id 4
    label "2-oxoglutarate"
  ]
  node [
    id 5
    label "l-aspartate"
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
    target 3
  ]
  edge [
    source 0
    target 5
  ]
  edge [
    source 1
    target 4
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
    source 1
    target 5
  ]
  edge [
    source 2
    target 4
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
    target 4
  ]
  edge [
    source 3
    target 5
  ]
  edge [
    source 4
    target 5
  ]
]

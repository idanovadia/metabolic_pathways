graph [
  label "negative"
  type "trainset"
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
    label "succinate"
  ]
  node [
    id 3
    label "2-oxoglutarate"
  ]
  node [
    id 4
    label "l-valine"
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
    source 0
    target 4
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 1
    target 3
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 1
    target 4
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 2
    target 4
  ]
  edge [
    source 3
    target 4
  ]
]

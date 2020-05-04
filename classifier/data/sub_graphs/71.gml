graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "l-phenylalanine"
  ]
  node [
    id 1
    label "glycine"
  ]
  node [
    id 2
    label "l-serine"
  ]
  node [
    id 3
    label "phosphate"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 3
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
    source 2
    target 3
  ]
]

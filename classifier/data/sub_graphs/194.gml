graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "l-alanine"
  ]
  node [
    id 2
    label "l-glutamate"
  ]
  node [
    id 3
    label "l-lysine"
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
]

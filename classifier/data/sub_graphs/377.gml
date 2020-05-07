graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "l-tyrosine"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "l-lysine"
  ]
  node [
    id 3
    label "l-cysteine"
  ]
  node [
    id 4
    label "shikimate"
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
    source 0
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

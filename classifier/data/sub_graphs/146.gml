graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "l-tryptophan"
  ]
  node [
    id 1
    label "benzoate"
  ]
  node [
    id 2
    label "shikimate"
  ]
  node [
    id 3
    label "l-alanine"
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

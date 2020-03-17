graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "shikimate"
  ]
  node [
    id 1
    label "l-tryptophan"
  ]
  node [
    id 2
    label "l-alanine"
  ]
  node [
    id 3
    label "benzoate"
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
]

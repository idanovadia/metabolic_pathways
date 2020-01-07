graph [
  label "random"
  node [
    id 0
    label "l-tryptophan"
  ]
  node [
    id 1
    label "l-alanine"
  ]
  node [
    id 2
    label "shikimate"
  ]
  node [
    id 3
    label "benzoate"
  ]
  node [
    id 4
    label "succinate"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 0
    target 4
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
]

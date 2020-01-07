graph [
  label "random"
  node [
    id 0
    label "l-cysteine"
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
    label "shikimate"
  ]
  node [
    id 4
    label "l-tyrosine"
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

graph [
  label "random"
  node [
    id 0
    label "l-methionine"
  ]
  node [
    id 1
    label "l-tyrosine"
  ]
  node [
    id 2
    label "l-alanine"
  ]
  node [
    id 3
    label "l-cysteine"
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

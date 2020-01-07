graph [
  label "random"
  node [
    id 0
    label "l-cysteine"
  ]
  node [
    id 1
    label "l-homoserine"
  ]
  node [
    id 2
    label "l-methionine"
  ]
  node [
    id 3
    label "phosphate"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
]

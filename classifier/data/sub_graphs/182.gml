graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "l-aspartate"
  ]
  node [
    id 1
    label "succinate"
  ]
  node [
    id 2
    label "phosphate"
  ]
  node [
    id 3
    label "l-cysteine"
  ]
  node [
    id 4
    label "l-methionine"
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
]

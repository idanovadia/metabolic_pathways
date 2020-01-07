graph [
  label "random"
  node [
    id 0
    label "l-methionine"
  ]
  node [
    id 1
    label "l-cysteine"
  ]
  node [
    id 2
    label "succinate"
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

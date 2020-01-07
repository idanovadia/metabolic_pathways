graph [
  label "random"
  node [
    id 0
    label "glycerol"
  ]
  node [
    id 1
    label "l-cysteine"
  ]
  node [
    id 2
    label "shikimate"
  ]
  node [
    id 3
    label "l-lysine"
  ]
  node [
    id 4
    label "l-alanine"
  ]
  node [
    id 5
    label "l-valine"
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 1
    target 5
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
  edge [
    source 4
    target 5
    weight 1
  ]
]

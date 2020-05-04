graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "l-alanine"
  ]
  node [
    id 1
    label "shikimate"
  ]
  node [
    id 2
    label "glycerol"
  ]
  node [
    id 3
    label "l-lysine"
  ]
  node [
    id 4
    label "l-valine"
  ]
  node [
    id 5
    label "l-cysteine"
  ]
  edge [
    source 0
    target 5
  ]
  edge [
    source 0
    target 4
  ]
  edge [
    source 0
    target 3
  ]
  edge [
    source 3
    target 5
  ]
  edge [
    source 3
    target 4
  ]
  edge [
    source 4
    target 5
  ]
]

graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "l-lysine"
  ]
  node [
    id 1
    label "l-valine"
  ]
  node [
    id 2
    label "l-alanine"
  ]
  node [
    id 3
    label "l-cysteine"
  ]
  node [
    id 4
    label "shikimate"
  ]
  node [
    id 5
    label "glycerol"
  ]
  edge [
    source 0
    target 2
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
    target 5
  ]
  edge [
    source 0
    target 4
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 1
    target 3
  ]
  edge [
    source 1
    target 5
  ]
  edge [
    source 1
    target 4
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 2
    target 5
  ]
  edge [
    source 2
    target 4
  ]
  edge [
    source 3
    target 5
  ]
  edge [
    source 3
    target 4
  ]
]

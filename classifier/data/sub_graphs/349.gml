graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "glycine"
  ]
  node [
    id 1
    label "l-alanine"
  ]
  node [
    id 2
    label "l-cysteine"
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
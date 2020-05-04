graph [
  label "positive"
  type "trainset"
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
    label "l-alanine"
  ]
  node [
    id 3
    label "phosphate"
  ]
  node [
    id 4
    label "glycine"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 2
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
    target 4
  ]
  edge [
    source 2
    target 4
  ]
]

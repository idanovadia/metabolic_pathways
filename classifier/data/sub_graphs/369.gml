graph [
  label "random"
  type "trainset"
  node [
    id 0
    label "benzoate"
  ]
  node [
    id 1
    label "beta;-alanine"
  ]
  node [
    id 2
    label "l-glutamine"
  ]
  node [
    id 3
    label "l-cysteine"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
]

graph [
  label "random"
  type "trainset"
  node [
    id 0
    label "l-tyrosine"
  ]
  node [
    id 1
    label "alpha;,alpha;-trehalose"
  ]
  node [
    id 2
    label "l-cysteine"
  ]
  node [
    id 3
    label "l-serine"
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

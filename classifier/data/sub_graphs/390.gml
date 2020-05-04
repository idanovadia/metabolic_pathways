graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "l-leucine"
  ]
  node [
    id 1
    label "l-isoleucine"
  ]
  node [
    id 2
    label "beta;-alanine"
  ]
  node [
    id 3
    label "glucose_6_phosphate"
  ]
  node [
    id 4
    label "glycerol"
  ]
  node [
    id 5
    label "benzoate"
  ]
  node [
    id 6
    label "2-oxoglutarate"
  ]
  node [
    id 7
    label "alpha;,alpha;-trehalose"
  ]
  edge [
    source 0
    target 5
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
    target 2
  ]
  edge [
    source 0
    target 7
  ]
  edge [
    source 1
    target 3
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 2
    target 7
  ]
  edge [
    source 3
    target 5
  ]
  edge [
    source 3
    target 7
  ]
  edge [
    source 5
    target 7
  ]
]

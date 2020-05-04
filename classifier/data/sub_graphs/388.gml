graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "beta;-alanine"
  ]
  node [
    id 1
    label "l-alanine"
  ]
  node [
    id 2
    label "glycerate_3_phosphate"
  ]
  node [
    id 3
    label "alpha;-tocopherol"
  ]
  node [
    id 4
    label "fructose"
  ]
  node [
    id 5
    label "l-aspartate"
  ]
  node [
    id 6
    label "alpha;,alpha;-trehalose"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 3
  ]
  edge [
    source 0
    target 6
  ]
  edge [
    source 1
    target 3
  ]
  edge [
    source 1
    target 6
  ]
  edge [
    source 3
    target 6
  ]
]

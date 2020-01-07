graph [
  label "random"
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
    label "fructose"
  ]
  node [
    id 4
    label "alpha;,alpha;-trehalose"
  ]
  node [
    id 5
    label "l-aspartate"
  ]
  node [
    id 6
    label "alpha;-tocopherol"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 0
    target 6
    weight 1
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 0
    target 4
    weight 1
  ]
  edge [
    source 1
    target 6
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 2
    target 6
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
  edge [
    source 4
    target 6
    weight 1
  ]
]

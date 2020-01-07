graph [
  label "random"
  node [
    id 0
    label "sucrose"
  ]
  node [
    id 1
    label "threonate"
  ]
  node [
    id 2
    label "glucose"
  ]
  node [
    id 3
    label "glucose_6_phosphate"
  ]
  node [
    id 4
    label "galactose"
  ]
  node [
    id 5
    label "l-tryptophan"
  ]
  node [
    id 6
    label "l-valine"
  ]
  node [
    id 7
    label "alpha;,alpha;-trehalose"
  ]
  edge [
    source 0
    target 7
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 1
    target 7
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
  edge [
    source 3
    target 7
    weight 1
  ]
  edge [
    source 3
    target 6
    weight 1
  ]
]

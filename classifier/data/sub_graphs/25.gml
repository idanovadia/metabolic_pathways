graph [
  label "random"
  node [
    id 0
    label "l-glutamine"
  ]
  node [
    id 1
    label "glucose"
  ]
  node [
    id 2
    label "phosphate"
  ]
  node [
    id 3
    label "l-glutamate"
  ]
  node [
    id 4
    label "alpha;,alpha;-trehalose"
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
    source 0
    target 2
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
]

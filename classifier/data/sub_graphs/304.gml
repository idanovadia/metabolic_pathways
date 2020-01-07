graph [
  label "random"
  node [
    id 0
    label "l-glutamine"
  ]
  node [
    id 1
    label "uracil"
  ]
  node [
    id 2
    label "phosphate"
  ]
  node [
    id 3
    label "l-glutamate"
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
    source 2
    target 3
    weight 1
  ]
]

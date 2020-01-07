graph [
  label "random"
  node [
    id 0
    label "l-asparagine"
  ]
  node [
    id 1
    label "phosphate"
  ]
  node [
    id 2
    label "l-aspartate"
  ]
  node [
    id 3
    label "l-glutamate"
  ]
  node [
    id 4
    label "l-glutamine"
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

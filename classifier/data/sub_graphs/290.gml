graph [
  label "random"
  node [
    id 0
    label "l-asparagine"
  ]
  node [
    id 1
    label "l-glutamine"
  ]
  node [
    id 2
    label "l-aspartate"
  ]
  node [
    id 3
    label "l-glutamate"
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

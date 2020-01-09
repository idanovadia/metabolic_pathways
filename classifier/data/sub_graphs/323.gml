graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "l-aspartate"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "l-asparagine"
  ]
  node [
    id 3
    label "l-glutamine"
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

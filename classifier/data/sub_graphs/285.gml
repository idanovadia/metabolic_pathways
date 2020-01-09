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
    label "l-glutamine"
  ]
  node [
    id 3
    label "phosphate"
  ]
  edge [
    source 0
    target 1
    weight 1
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

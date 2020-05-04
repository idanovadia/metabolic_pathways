graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "l-glutamate"
  ]
  node [
    id 1
    label "l-aspartate"
  ]
  node [
    id 2
    label "l-glutamine"
  ]
  node [
    id 3
    label "l-asparagine"
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
]

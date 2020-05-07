graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "fumarate"
  ]
  node [
    id 1
    label "succinate"
  ]
  node [
    id 2
    label "(s)-malate"
  ]
  node [
    id 3
    label "l-glutamate"
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 1
    target 2
  ]
]

graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "(s)-malate"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "succinate"
  ]
  node [
    id 3
    label "fumarate"
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

graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "l-aspartate"
  ]
  node [
    id 1
    label "phosphate"
  ]
  node [
    id 2
    label "fumarate"
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

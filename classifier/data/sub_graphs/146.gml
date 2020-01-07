graph [
  label "random"
  node [
    id 0
    label "l-glutamine"
  ]
  node [
    id 1
    label "phosphate"
  ]
  node [
    id 2
    label "l-glutamate"
  ]
  node [
    id 3
    label "fumarate"
  ]
  node [
    id 4
    label "l-aspartate"
  ]
  node [
    id 5
    label "glycine"
  ]
  edge [
    source 0
    target 4
    weight 1
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
]

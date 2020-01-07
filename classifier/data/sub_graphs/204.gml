graph [
  label "random"
  node [
    id 0
    label "5-oxoproline"
  ]
  node [
    id 1
    label "glycine"
  ]
  node [
    id 2
    label "l-cysteine"
  ]
  node [
    id 3
    label "phosphate"
  ]
  node [
    id 4
    label "l-glutamate"
  ]
  edge [
    source 0
    target 4
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
    source 3
    target 4
    weight 1
  ]
]

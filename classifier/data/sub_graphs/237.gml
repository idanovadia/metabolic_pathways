graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "glycine"
  ]
  node [
    id 1
    label "phosphate"
  ]
  node [
    id 2
    label "l-cysteine"
  ]
  node [
    id 3
    label "l-glutamate"
  ]
  node [
    id 4
    label "5-oxoproline"
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
]

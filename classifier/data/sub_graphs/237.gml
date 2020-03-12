graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "l-glutamate"
  ]
  node [
    id 1
    label "5-oxoproline"
  ]
  node [
    id 2
    label "l-cysteine"
  ]
  node [
    id 3
    label "glycine"
  ]
  node [
    id 4
    label "phosphate"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 0
    target 4
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
]

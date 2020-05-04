graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "l-methionine"
  ]
  node [
    id 1
    label "l-ascorbate"
  ]
  node [
    id 2
    label "phosphate"
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
    target 2
  ]
]

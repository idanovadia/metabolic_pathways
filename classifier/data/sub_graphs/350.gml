graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "l-threonine"
  ]
  node [
    id 1
    label "l-homoserine"
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

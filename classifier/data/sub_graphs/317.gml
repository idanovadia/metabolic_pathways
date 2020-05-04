graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "sucrose"
  ]
  node [
    id 1
    label "phosphate"
  ]
  node [
    id 2
    label "glucose"
  ]
  node [
    id 3
    label "fructose 1,6-bisphosphate"
  ]
  edge [
    source 0
    target 3
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

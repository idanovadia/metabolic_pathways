graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "fructose 1,6-bisphosphate"
  ]
  node [
    id 2
    label "glucose"
  ]
  node [
    id 3
    label "sucrose"
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
]

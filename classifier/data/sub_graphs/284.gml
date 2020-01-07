graph [
  label "random"
  node [
    id 0
    label "glucose"
  ]
  node [
    id 1
    label "phosphate"
  ]
  node [
    id 2
    label "fructose 1,6-bisphosphate"
  ]
  node [
    id 3
    label "sucrose"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
]

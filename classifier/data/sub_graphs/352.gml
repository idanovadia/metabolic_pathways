graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "alpha;,alpha;-trehalose"
  ]
  node [
    id 1
    label "phosphate"
  ]
  node [
    id 2
    label "glucose"
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

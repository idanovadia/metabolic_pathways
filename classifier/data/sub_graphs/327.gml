graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "putrescine"
  ]
  node [
    id 1
    label "2-oxoglutarate"
  ]
  node [
    id 2
    label "succinate"
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

graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "l-serine"
  ]
  node [
    id 1
    label "l-threonine"
  ]
  node [
    id 2
    label "2-oxoglutarate"
  ]
  node [
    id 3
    label "l-glutamate"
  ]
  node [
    id 4
    label "glycine"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 4
  ]
  edge [
    source 1
    target 4
  ]
]

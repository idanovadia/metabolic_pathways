graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "l-threonine"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "l-serine"
  ]
  node [
    id 3
    label "2-oxoglutarate"
  ]
  node [
    id 4
    label "glycine"
  ]
  edge [
    source 0
    target 4
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 2
    target 4
  ]
]

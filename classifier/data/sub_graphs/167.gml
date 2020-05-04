graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "l-isoleucine"
  ]
  node [
    id 1
    label "l-threonine"
  ]
  node [
    id 2
    label "l-glutamate"
  ]
  node [
    id 3
    label "2-oxoglutarate"
  ]
  node [
    id 4
    label "phosphate"
  ]
  node [
    id 5
    label "glycine"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 5
  ]
  edge [
    source 1
    target 5
  ]
]

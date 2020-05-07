graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "l-glutamate"
  ]
  node [
    id 1
    label "l-valine"
  ]
  node [
    id 2
    label "l-alanine"
  ]
  node [
    id 3
    label "l-cysteine"
  ]
  node [
    id 4
    label "2-oxoglutarate"
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 1
    target 3
  ]
  edge [
    source 2
    target 3
  ]
]

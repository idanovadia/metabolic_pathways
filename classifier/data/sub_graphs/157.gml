graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "l-alanine"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "l-valine"
  ]
  node [
    id 3
    label "2-oxoglutarate"
  ]
  node [
    id 4
    label "l-cysteine"
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

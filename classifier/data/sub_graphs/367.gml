graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "l-tyrosine"
  ]
  node [
    id 1
    label "l-cysteine"
  ]
  node [
    id 2
    label "dehydroascorbate (bicyclic form)"
  ]
  node [
    id 3
    label "l-lysine"
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
    source 0
    target 3
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

graph [
  label "random"
  node [
    id 0
    label "dehydroascorbate (bicyclic form)"
  ]
  node [
    id 1
    label "glycerol"
  ]
  node [
    id 2
    label "2-oxoglutarate"
  ]
  node [
    id 3
    label "l-glutamate"
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
]

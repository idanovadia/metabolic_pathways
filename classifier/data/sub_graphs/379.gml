graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "d-glycerate"
  ]
  node [
    id 1
    label "l-leucine"
  ]
  node [
    id 2
    label "dehydroascorbate (bicyclic form)"
  ]
  node [
    id 3
    label "uracil"
  ]
  node [
    id 4
    label "2-oxoglutarate"
  ]
  node [
    id 5
    label "alpha;-tocopherol"
  ]
  edge [
    source 0
    target 5
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
    source 0
    target 3
  ]
  edge [
    source 1
    target 5
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
    target 5
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 3
    target 5
  ]
]

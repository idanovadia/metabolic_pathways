graph [
  label "random"
  node [
    id 0
    label "l-leucine"
  ]
  node [
    id 1
    label "alpha;-tocopherol"
  ]
  node [
    id 2
    label "2-oxoglutarate"
  ]
  node [
    id 3
    label "uracil"
  ]
  node [
    id 4
    label "dehydroascorbate (bicyclic form)"
  ]
  node [
    id 5
    label "d-glycerate"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 0
    target 4
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
]

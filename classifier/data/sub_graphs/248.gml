graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "2-oxoglutarate"
  ]
  node [
    id 1
    label "phosphate"
  ]
  node [
    id 2
    label "cis-aconitate"
  ]
  node [
    id 3
    label "l-glutamate"
  ]
  node [
    id 4
    label "d-threo-isocitrate"
  ]
  node [
    id 5
    label "citrate"
  ]
  node [
    id 6
    label "l-glutamine"
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 1
    target 5
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 1
    target 6
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
  edge [
    source 3
    target 6
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
  edge [
    source 4
    target 5
    weight 1
  ]
  edge [
    source 4
    target 6
    weight 1
  ]
  edge [
    source 5
    target 6
    weight 1
  ]
]

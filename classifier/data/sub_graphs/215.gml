graph [
  label "random"
  node [
    id 0
    label "l-glutamine"
  ]
  node [
    id 1
    label "phosphate"
  ]
  node [
    id 2
    label "l-glutamate"
  ]
  node [
    id 3
    label "d-threo-isocitrate"
  ]
  node [
    id 4
    label "cis-aconitate"
  ]
  node [
    id 5
    label "citrate"
  ]
  node [
    id 6
    label "2-oxoglutarate"
  ]
  edge [
    source 0
    target 5
    weight 1
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 1
    target 5
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 2
    target 5
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
  edge [
    source 4
    target 6
    weight 1
  ]
]

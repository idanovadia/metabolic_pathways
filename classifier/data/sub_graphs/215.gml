graph [
  label "random"
  node [
    id 0
    label "2-oxoglutarate"
  ]
  node [
    id 1
    label "citrate"
  ]
  node [
    id 2
    label "cis-aconitate"
  ]
  node [
    id 3
    label "phosphate"
  ]
  node [
    id 4
    label "d-threo-isocitrate"
  ]
  node [
    id 5
    label "l-glutamate"
  ]
  node [
    id 6
    label "l-glutamine"
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
]

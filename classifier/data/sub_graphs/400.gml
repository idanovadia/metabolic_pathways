graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "d-threo-isocitrate"
  ]
  node [
    id 1
    label "threonate"
  ]
  node [
    id 2
    label "glucose_6_phosphate"
  ]
  node [
    id 3
    label "l-tyrosine"
  ]
  node [
    id 4
    label "l-lysine"
  ]
  node [
    id 5
    label "l-glutamine"
  ]
  node [
    id 6
    label "l-valine"
  ]
  node [
    id 7
    label "2-oxoglutarate"
  ]
  node [
    id 8
    label "phosphate"
  ]
  node [
    id 9
    label "glycine"
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 2
    target 9
  ]
  edge [
    source 2
    target 6
  ]
  edge [
    source 2
    target 4
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 3
    target 4
  ]
  edge [
    source 3
    target 6
  ]
  edge [
    source 3
    target 9
  ]
  edge [
    source 4
    target 9
  ]
  edge [
    source 4
    target 6
  ]
  edge [
    source 6
    target 9
  ]
]

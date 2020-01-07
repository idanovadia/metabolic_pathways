graph [
  label "random"
  node [
    id 0
    label "l-glutamine"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "l-phenylalanine"
  ]
  node [
    id 3
    label "glycine"
  ]
  node [
    id 4
    label "2-oxoglutarate"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
]

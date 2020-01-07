graph [
  label "random"
  node [
    id 0
    label "l-phenylalanine"
  ]
  node [
    id 1
    label "2-oxoglutarate"
  ]
  node [
    id 2
    label "shikimate"
  ]
  node [
    id 3
    label "l-tyrosine"
  ]
  node [
    id 4
    label "l-serine"
  ]
  node [
    id 5
    label "l-tryptophan"
  ]
  node [
    id 6
    label "phosphate"
  ]
  node [
    id 7
    label "l-glutamate"
  ]
  node [
    id 8
    label "l-glutamine"
  ]
  edge [
    source 0
    target 4
    weight 1
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
  edge [
    source 6
    target 7
    weight 1
  ]
]

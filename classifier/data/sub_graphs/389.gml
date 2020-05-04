graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "l-leucine"
  ]
  node [
    id 1
    label "maltitol"
  ]
  node [
    id 2
    label "l-phenylalanine"
  ]
  node [
    id 3
    label "sucrose"
  ]
  node [
    id 4
    label "inositol"
  ]
  node [
    id 5
    label "gaba"
  ]
  node [
    id 6
    label "alpha;,alpha;-trehalose"
  ]
  node [
    id 7
    label "citrate"
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 0
    target 5
  ]
  edge [
    source 0
    target 6
  ]
  edge [
    source 2
    target 5
  ]
  edge [
    source 2
    target 6
  ]
  edge [
    source 5
    target 6
  ]
]

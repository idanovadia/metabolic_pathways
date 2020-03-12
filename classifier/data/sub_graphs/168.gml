graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "shikimate"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "l-tryptophan"
  ]
  node [
    id 3
    label "l-glutamine"
  ]
  node [
    id 4
    label "phosphate"
  ]
  node [
    id 5
    label "l-serine"
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
    source 1
    target 3
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 2
    target 5
    weight 1
  ]
  edge [
    source 3
    target 4
    weight 1
  ]
]

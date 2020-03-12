graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "uracil"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "d-ribofuranose"
  ]
  node [
    id 3
    label "l-glutamine"
  ]
  node [
    id 4
    label "phosphate"
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
    source 3
    target 4
    weight 1
  ]
]

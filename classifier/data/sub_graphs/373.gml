graph [
  label "random"
  type "trainset"
  node [
    id 0
    label "erythritol"
  ]
  node [
    id 1
    label "d-glycerate"
  ]
  node [
    id 2
    label "l-cysteine"
  ]
  node [
    id 3
    label "l-glutamate"
  ]
  node [
    id 4
    label "threonate"
  ]
  edge [
    source 0
    target 2
    weight 1
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
    target 2
    weight 1
  ]
  edge [
    source 1
    target 4
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
]

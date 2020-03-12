graph [
  label "random"
  type "trainset"
  node [
    id 0
    label "d-glycerate"
  ]
  node [
    id 1
    label "threonate"
  ]
  node [
    id 2
    label "l-glutamate"
  ]
  node [
    id 3
    label "erythritol"
  ]
  node [
    id 4
    label "l-cysteine"
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
    source 0
    target 1
    weight 1
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
    target 4
    weight 1
  ]
]

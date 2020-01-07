graph [
  label "random"
  node [
    id 0
    label "l-cysteine"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "threonate"
  ]
  node [
    id 3
    label "d-glycerate"
  ]
  node [
    id 4
    label "erythritol"
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
    target 2
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

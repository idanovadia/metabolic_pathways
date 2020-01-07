graph [
  label "random"
  node [
    id 0
    label "erythritol"
  ]
  node [
    id 1
    label "l-cysteine"
  ]
  node [
    id 2
    label "threonate"
  ]
  node [
    id 3
    label "l-glutamate"
  ]
  node [
    id 4
    label "d-glycerate"
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
    source 0
    target 2
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
]

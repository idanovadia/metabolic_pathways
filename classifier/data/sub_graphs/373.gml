graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "threonate"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "erythritol"
  ]
  node [
    id 3
    label "d-glycerate"
  ]
  node [
    id 4
    label "l-cysteine"
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 0
    target 3
  ]
  edge [
    source 2
    target 4
  ]
  edge [
    source 2
    target 3
  ]
]

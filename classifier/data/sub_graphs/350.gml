graph [
  label "random"
  node [
    id 0
    label "l-leucine"
  ]
  node [
    id 1
    label "alpha;-tocopherol"
  ]
  node [
    id 2
    label "erythritol"
  ]
  node [
    id 3
    label "succinate"
  ]
  node [
    id 4
    label "threonate"
  ]
  node [
    id 5
    label "shikimate"
  ]
  node [
    id 6
    label "maltitol"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 0
    target 2
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

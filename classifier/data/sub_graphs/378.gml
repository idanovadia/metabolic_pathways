graph [
  label "random"
  type "trainset"
  node [
    id 0
    label "fructose"
  ]
  node [
    id 1
    label "glycerate_3_phosphate"
  ]
  node [
    id 2
    label "l-asparagine"
  ]
  node [
    id 3
    label "l-leucine"
  ]
  node [
    id 4
    label "erythritol"
  ]
  node [
    id 5
    label "citrate"
  ]
  edge [
    source 0
    target 5
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
    source 1
    target 3
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

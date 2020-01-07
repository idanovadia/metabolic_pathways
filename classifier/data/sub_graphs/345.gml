graph [
  label "random"
  node [
    id 0
    label "l-asparagine"
  ]
  node [
    id 1
    label "l-leucine"
  ]
  node [
    id 2
    label "glycerate_3_phosphate"
  ]
  node [
    id 3
    label "fructose"
  ]
  node [
    id 4
    label "citrate"
  ]
  node [
    id 5
    label "erythritol"
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
    source 0
    target 1
    weight 1
  ]
  edge [
    source 1
    target 5
    weight 1
  ]
  edge [
    source 1
    target 2
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

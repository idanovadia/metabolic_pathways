graph [
  label "random"
  node [
    id 0
    label "l-leucine"
  ]
  node [
    id 1
    label "glycerate_3_phosphate"
  ]
  node [
    id 2
    label "erythritol"
  ]
  node [
    id 3
    label "citrate"
  ]
  node [
    id 4
    label "l-asparagine"
  ]
  node [
    id 5
    label "fructose"
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
  edge [
    source 3
    target 5
    weight 1
  ]
]

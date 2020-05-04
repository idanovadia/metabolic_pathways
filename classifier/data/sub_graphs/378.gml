graph [
  label "negative"
  type "trainset"
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
    label "erythritol"
  ]
  node [
    id 5
    label "citrate"
  ]
  edge [
    source 0
    target 4
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 1
    target 4
  ]
  edge [
    source 3
    target 5
  ]
]

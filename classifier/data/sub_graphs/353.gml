graph [
  label "random"
  node [
    id 0
    label "l-leucine"
  ]
  node [
    id 1
    label "benzoate"
  ]
  node [
    id 2
    label "erythritol"
  ]
  node [
    id 3
    label "glycerol"
  ]
  node [
    id 4
    label "dehydroascorbate (bicyclic form)"
  ]
  node [
    id 5
    label "l-glutamate"
  ]
  node [
    id 6
    label "l-glutamine"
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
    source 1
    target 4
    weight 1
  ]
  edge [
    source 1
    target 2
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
]

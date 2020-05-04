graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "l-leucine"
  ]
  node [
    id 1
    label "glycerol"
  ]
  node [
    id 2
    label "benzoate"
  ]
  node [
    id 3
    label "dehydroascorbate (bicyclic form)"
  ]
  node [
    id 4
    label "l-glutamine"
  ]
  node [
    id 5
    label "erythritol"
  ]
  node [
    id 6
    label "l-glutamate"
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
    source 0
    target 5
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 2
    target 5
  ]
  edge [
    source 3
    target 5
  ]
]

graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "l-isoleucine"
  ]
  node [
    id 1
    label "l-leucine"
  ]
  node [
    id 2
    label "l-phenylalanine"
  ]
  node [
    id 3
    label "l-glutamine"
  ]
  node [
    id 4
    label "l-valine"
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 4
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 1
    target 4
  ]
  edge [
    source 2
    target 4
  ]
]

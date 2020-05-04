graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "l-leucine"
  ]
  node [
    id 1
    label "l-isoleucine"
  ]
  node [
    id 2
    label "l-glutamine"
  ]
  node [
    id 3
    label "l-valine"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 3
  ]
  edge [
    source 1
    target 3
  ]
]

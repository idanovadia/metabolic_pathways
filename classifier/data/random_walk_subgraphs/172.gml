graph [
  label "negative"
  type "trainset"
  name "172.gml"
  node [
    id 0
    label "galactose"
  ]
  node [
    id 1
    label "l-glutamine"
  ]
  node [
    id 2
    label "phosphate"
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
]
graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "gdp-alpha;-d-mannose"
  ]
  node [
    id 1
    label "phosphate"
  ]
  node [
    id 2
    label "glucose"
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
    target 2
    weight 1
  ]
]

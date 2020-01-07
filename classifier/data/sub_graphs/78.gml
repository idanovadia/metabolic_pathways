graph [
  label "random"
  node [
    id 0
    label "glucose"
  ]
  node [
    id 1
    label "phosphate"
  ]
  node [
    id 2
    label "gdp-alpha;-d-mannose"
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

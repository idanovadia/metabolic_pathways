graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "gdp-alpha;-d-mannose"
  ]
  node [
    id 1
    label "l-ascorbate"
  ]
  node [
    id 2
    label "phosphate"
  ]
  node [
    id 3
    label "galactose"
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 2
    target 3
    weight 1
  ]
]

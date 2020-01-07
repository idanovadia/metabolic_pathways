graph [
  label "random"
  node [
    id 0
    label "phosphate"
  ]
  node [
    id 1
    label "galactose"
  ]
  node [
    id 2
    label "l-ascorbate"
  ]
  node [
    id 3
    label "gdp-alpha;-d-mannose"
  ]
  edge [
    source 0
    target 1
    weight 1
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
]

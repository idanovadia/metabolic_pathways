graph [
  label "random"
  type "trainset"
  name "406.gml"
  node [
    id 0
    label "l-glutamate"
  ]
  node [
    id 1
    label "gdp-alpha;-d-mannose"
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

graph [
  label "positive"
  type "trainset"
  node [
    id 0
    label "galactose"
  ]
  node [
    id 1
    label "gdp-beta;-l-fucose"
  ]
  node [
    id 2
    label "gdp-alpha;-d-mannose"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 2
  ]
  edge [
    source 1
    target 2
  ]
]

graph [
  label "random"
  node [
    id 0
    label "2-oxoglutarate"
  ]
  node [
    id 1
    label "l-glutamate"
  ]
  node [
    id 2
    label "gdp-beta;-l-fucose"
  ]
  node [
    id 3
    label "gdp-alpha;-d-mannose"
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 1
    target 3
    weight 1
  ]
]

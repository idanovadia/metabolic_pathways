graph [
  label "negative"
  type "trainset"
  node [
    id 0
    label "2-oxoglutarate"
  ]
  node [
    id 1
    label "gdp-alpha;-d-mannose"
  ]
  node [
    id 2
    label "l-glutamate"
  ]
  node [
    id 3
    label "gdp-beta;-l-fucose"
  ]
  edge [
    source 0
    target 3
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 1
    target 3
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 2
    target 3
  ]
]

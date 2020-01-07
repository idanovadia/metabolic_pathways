graph [
  label "random"
  node [
    id 0
    label "l-leucine"
  ]
  node [
    id 1
    label "glycerate_3_phosphate"
  ]
  node [
    id 2
    label "benzoate"
  ]
  node [
    id 3
    label "gdp-alpha;-d-mannose"
  ]
  node [
    id 4
    label "l-cysteine"
  ]
  node [
    id 5
    label "udp-alpha;-d-galacturonate"
  ]
  node [
    id 6
    label "gdp-beta;-l-fucose"
  ]
  node [
    id 7
    label "l-aspartate"
  ]
  node [
    id 8
    label "l-glutamine"
  ]
  edge [
    source 0
    target 2
    weight 1
  ]
  edge [
    source 0
    target 4
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
  edge [
    source 2
    target 6
    weight 1
  ]
  edge [
    source 2
    target 5
    weight 1
  ]
  edge [
    source 4
    target 5
    weight 1
  ]
  edge [
    source 5
    target 6
    weight 1
  ]
]

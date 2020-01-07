graph [
  label "random"
  node [
    id 0
    label "sucrose"
  ]
  node [
    id 1
    label "glycerate_3_phosphate"
  ]
  node [
    id 2
    label "gdp-alpha;-d-mannose"
  ]
  node [
    id 3
    label "maltose"
  ]
  node [
    id 4
    label "glucose"
  ]
  node [
    id 5
    label "glucose_6_phosphate"
  ]
  node [
    id 6
    label "inositol"
  ]
  node [
    id 7
    label "l-aspartate"
  ]
  node [
    id 8
    label "l-glutamate"
  ]
  node [
    id 9
    label "maltitol"
  ]
  node [
    id 10
    label "fructose"
  ]
  edge [
    source 0
    target 3
    weight 1
  ]
  edge [
    source 2
    target 10
    weight 1
  ]
  edge [
    source 2
    target 4
    weight 1
  ]
  edge [
    source 3
    target 5
    weight 1
  ]
  edge [
    source 4
    target 10
    weight 1
  ]
  edge [
    source 7
    target 8
    weight 1
  ]
]

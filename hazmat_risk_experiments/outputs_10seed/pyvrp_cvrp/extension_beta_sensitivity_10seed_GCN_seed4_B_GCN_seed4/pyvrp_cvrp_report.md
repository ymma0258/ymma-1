# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.772931 | 0.000% | 0.256644 | 3.007084 | 0.249171 | 0.861805 | 89.101% |
| 0.5 | 0 | 166560.6 | 13.514% | 6.095969 | 30.514% | 0.165595 | 2.045723 | 0.211153 | 0.847840 | 86.365% |
| 1 | 0 | 180642.3 | 23.111% | 4.402333 | 49.819% | 0.093574 | 1.586136 | 0.287053 | 0.822655 | 81.768% |
| 1.5 | 0 | 190902.3 | 30.104% | 3.743012 | 57.335% | 0.078601 | 1.499969 | 0.330206 | 0.804493 | 78.894% |
| 2 | 0 | 199890.9 | 36.230% | 3.428734 | 60.917% | 0.072126 | 1.493047 | 0.358960 | 0.791632 | 76.888% |
| 3 | 0 | 216662.1 | 47.659% | 3.268267 | 62.746% | 0.067724 | 1.474618 | 0.361196 | 0.783541 | 75.670% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

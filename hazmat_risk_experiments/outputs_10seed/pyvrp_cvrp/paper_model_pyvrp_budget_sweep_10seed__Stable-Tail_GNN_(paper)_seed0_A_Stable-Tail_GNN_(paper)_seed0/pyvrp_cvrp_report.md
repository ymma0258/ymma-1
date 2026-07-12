# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.5 | 0.000% | 7.479473 | 0.000% | 0.221981 | 2.451000 | 0.228168 | 0.884969 | 90.260% |
| 0.25 | 0 | 142519.5 | 6.254% | 4.753996 | 36.439% | 0.143193 | 1.523043 | 0.210267 | 0.863344 | 86.738% |
| 0.5 | 0 | 148594.6 | 10.783% | 3.498211 | 53.229% | 0.101547 | 1.388146 | 0.316560 | 0.832352 | 82.259% |
| 1 | 0 | 156378.5 | 16.586% | 2.351077 | 68.566% | 0.050525 | 0.925734 | 0.292325 | 0.780557 | 74.380% |
| 2 | 0 | 168425.5 | 25.567% | 1.785452 | 76.129% | 0.033521 | 0.564606 | 0.222734 | 0.730034 | 66.587% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

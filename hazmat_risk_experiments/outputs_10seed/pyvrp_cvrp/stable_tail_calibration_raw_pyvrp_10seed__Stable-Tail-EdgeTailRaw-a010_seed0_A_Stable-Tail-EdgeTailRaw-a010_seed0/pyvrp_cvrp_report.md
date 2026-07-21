# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.5 | 0.000% | 8.040557 | 0.000% | 0.250928 | 2.431011 | 0.196936 | 0.883481 | 90.252% |
| 0.25 | 0 | 142726.6 | 6.144% | 4.609515 | 42.672% | 0.138318 | 1.741597 | 0.270626 | 0.861332 | 86.421% |
| 0.5 | 0 | 148405.8 | 10.368% | 3.669492 | 54.363% | 0.105332 | 1.435512 | 0.315625 | 0.836434 | 83.099% |
| 1 | 0 | 156366.9 | 16.289% | 2.329494 | 71.028% | 0.054305 | 0.981082 | 0.301693 | 0.776538 | 73.797% |
| 2 | 0 | 168203.1 | 25.091% | 1.801936 | 77.589% | 0.033235 | 0.567403 | 0.225916 | 0.726467 | 66.250% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

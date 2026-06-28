# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 9.468694 | 0.000% | 0.293122 | 3.264840 | 0.243403 | 0.879964 | 90.860% |
| 1 | 0 | 176122.3 | 20.450% | 4.070030 | 57.016% | 0.109089 | 1.354147 | 0.307477 | 0.838555 | 81.632% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

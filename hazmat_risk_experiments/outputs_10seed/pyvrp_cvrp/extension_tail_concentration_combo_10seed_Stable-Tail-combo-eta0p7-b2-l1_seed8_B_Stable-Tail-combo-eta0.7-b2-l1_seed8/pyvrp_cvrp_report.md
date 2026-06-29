# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.420933 | 0.000% | 0.217788 | 2.362199 | 0.193787 | 0.878179 | 89.055% |
| 2 | 1 | 205710.0 | 40.195% | 2.340103 | 68.466% | 0.047479 | 0.891483 | 0.295630 | 0.776975 | 71.774% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

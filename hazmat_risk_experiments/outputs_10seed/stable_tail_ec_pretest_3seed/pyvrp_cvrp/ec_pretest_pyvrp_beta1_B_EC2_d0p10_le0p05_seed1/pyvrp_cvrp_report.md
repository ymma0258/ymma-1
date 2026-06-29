# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.096012 | 0.000% | 0.303870 | 3.237497 | 0.205830 | 0.872603 | 91.410% |
| 1 | 0 | 179711.3 | 22.477% | 4.464516 | 55.779% | 0.116708 | 1.561517 | 0.282196 | 0.845583 | 83.295% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

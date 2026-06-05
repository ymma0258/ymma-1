# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 146531.2 | 0.000% | 8.406688 | 0.000% | 0.226655 | 2.752095 | 0.219798 | 0.841198 | 87.350% |
| 1 | 178524.6 | 21.834% | 3.518651 | 58.145% | 0.071146 | 1.301935 | 0.273759 | 0.713398 | 70.858% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

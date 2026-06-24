# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.738460 | 0.000% | 0.230912 | 2.502142 | 0.204507 | 0.828061 | 85.600% |
| 1 | 0 | 176324.0 | 20.168% | 4.055889 | 47.588% | 0.095951 | 1.309024 | 0.239618 | 0.746169 | 74.960% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

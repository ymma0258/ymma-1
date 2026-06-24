# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.611109 | 0.000% | 0.200874 | 1.942227 | 0.163165 | 0.832713 | 85.365% |
| 1 | 0 | 157460.6 | 17.510% | 2.603837 | 60.614% | 0.056435 | 0.958261 | 0.266058 | 0.685226 | 66.500% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

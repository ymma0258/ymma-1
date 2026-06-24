# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.113315 | 0.000% | 0.239901 | 2.439197 | 0.151719 | 0.855033 | 88.172% |
| 1 | 0 | 159989.6 | 19.397% | 3.239510 | 60.072% | 0.069224 | 1.114422 | 0.287200 | 0.762175 | 75.399% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

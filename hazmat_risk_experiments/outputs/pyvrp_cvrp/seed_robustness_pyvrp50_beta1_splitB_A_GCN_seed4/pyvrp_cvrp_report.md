# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 7.965716 | 0.000% | 0.251843 | 2.536680 | 0.184517 | 0.861122 | 89.217% |
| 1 | 0 | 161475.6 | 20.507% | 3.322216 | 58.294% | 0.072167 | 1.158712 | 0.300712 | 0.794956 | 78.193% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

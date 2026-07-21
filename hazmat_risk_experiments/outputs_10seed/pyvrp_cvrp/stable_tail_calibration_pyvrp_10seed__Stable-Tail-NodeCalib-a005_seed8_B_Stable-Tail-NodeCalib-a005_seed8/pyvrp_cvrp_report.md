# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.0 | 0.000% | 7.465092 | 0.000% | 0.224253 | 2.312711 | 0.196613 | 0.857010 | 87.455% |
| 0.25 | 0 | 156840.6 | 6.503% | 5.914923 | 20.766% | 0.141156 | 1.863063 | 0.195805 | 0.852208 | 86.022% |
| 0.5 | 0 | 165462.3 | 12.358% | 5.084197 | 31.894% | 0.122971 | 1.604350 | 0.220350 | 0.839997 | 84.296% |
| 1 | 0 | 176479.3 | 19.839% | 3.296935 | 55.835% | 0.083362 | 1.249217 | 0.287098 | 0.791997 | 76.891% |
| 2 | 0 | 191577.4 | 30.091% | 2.531016 | 66.095% | 0.056320 | 0.726562 | 0.187015 | 0.754925 | 71.094% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

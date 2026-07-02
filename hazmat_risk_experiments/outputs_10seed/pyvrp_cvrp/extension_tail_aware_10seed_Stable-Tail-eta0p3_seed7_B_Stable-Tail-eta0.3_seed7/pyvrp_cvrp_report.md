# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 12.102753 | 0.000% | 0.231252 | 3.920632 | 0.203885 | 0.881280 | 90.809% |
| 1 | 0 | 177320.5 | 20.847% | 4.525093 | 62.611% | 0.072740 | 1.522671 | 0.273105 | 0.825457 | 79.265% |
| 2 | 0 | 193579.4 | 31.928% | 4.058090 | 66.470% | 0.066722 | 1.235088 | 0.236544 | 0.814561 | 77.264% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

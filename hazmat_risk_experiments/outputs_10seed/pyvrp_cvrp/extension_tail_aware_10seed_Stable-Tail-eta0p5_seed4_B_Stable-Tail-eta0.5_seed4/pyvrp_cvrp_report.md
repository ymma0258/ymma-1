# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 11.985039 | 0.000% | 0.278654 | 3.834561 | 0.197007 | 0.877996 | 89.989% |
| 1 | 0 | 176882.4 | 20.549% | 4.972851 | 58.508% | 0.071576 | 1.817168 | 0.307676 | 0.819331 | 79.183% |
| 2 | 0 | 192418.2 | 31.137% | 3.952552 | 67.021% | 0.057048 | 1.778773 | 0.356775 | 0.791195 | 75.014% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

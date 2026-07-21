# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 7.238511 | 0.000% | 0.215338 | 2.534885 | 0.252315 | 0.883205 | 90.111% |
| 0.25 | 0 | 142516.8 | 6.199% | 4.217976 | 41.729% | 0.127240 | 1.464844 | 0.237948 | 0.858072 | 85.945% |
| 0.5 | 0 | 148220.7 | 10.449% | 3.481135 | 51.908% | 0.102266 | 1.382720 | 0.319987 | 0.836625 | 82.950% |
| 1 | 0 | 156055.5 | 16.287% | 2.334445 | 67.750% | 0.056455 | 0.928366 | 0.307482 | 0.782243 | 74.937% |
| 2 | 0 | 168301.7 | 25.413% | 1.727284 | 76.138% | 0.032312 | 0.541046 | 0.199077 | 0.732802 | 67.086% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

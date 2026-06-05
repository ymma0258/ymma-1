# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 7.112312 | 0.000% | 0.220839 | 2.386151 | 0.237350 | 0.877486 | 89.797% |
| 0.25 | 0 | 142923.0 | 6.661% | 5.336392 | 24.970% | 0.158682 | 1.691537 | 0.173777 | 0.871078 | 87.898% |
| 0.5 | 0 | 148677.2 | 10.955% | 3.998488 | 43.781% | 0.123032 | 2.072171 | 0.389064 | 0.842896 | 84.478% |
| 1 | 0 | 156742.0 | 16.974% | 2.349958 | 66.959% | 0.050820 | 0.865722 | 0.257270 | 0.790399 | 75.196% |
| 2 | 0 | 167859.4 | 25.271% | 1.635318 | 77.007% | 0.028551 | 0.453555 | 0.185790 | 0.702405 | 62.558% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

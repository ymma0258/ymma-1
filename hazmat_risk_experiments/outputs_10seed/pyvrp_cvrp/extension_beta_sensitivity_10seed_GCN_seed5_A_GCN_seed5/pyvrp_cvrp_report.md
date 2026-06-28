# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.793624 | 0.000% | 0.194298 | 2.078779 | 0.183395 | 0.864754 | 88.450% |
| 0.5 | 0 | 148408.7 | 10.755% | 3.812006 | 43.888% | 0.103797 | 1.429732 | 0.282650 | 0.828468 | 83.059% |
| 1 | 0 | 156669.3 | 16.919% | 2.573161 | 62.124% | 0.067494 | 0.943918 | 0.258365 | 0.770789 | 74.948% |
| 1.5 | 0 | 163491.9 | 22.011% | 2.406301 | 64.580% | 0.057018 | 0.888868 | 0.284904 | 0.762555 | 73.612% |
| 2 | 0 | 170053.4 | 26.908% | 2.222814 | 67.281% | 0.044210 | 0.718142 | 0.247714 | 0.749032 | 71.266% |
| 3 | 0 | 181229.9 | 35.249% | 2.110296 | 68.937% | 0.038226 | 0.681301 | 0.245538 | 0.734505 | 68.851% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

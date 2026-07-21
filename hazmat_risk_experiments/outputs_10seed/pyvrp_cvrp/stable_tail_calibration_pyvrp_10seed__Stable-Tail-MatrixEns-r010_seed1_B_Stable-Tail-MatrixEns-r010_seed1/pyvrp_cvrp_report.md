# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 8.756386 | 0.000% | 0.276636 | 3.035558 | 0.253267 | 0.872997 | 89.860% |
| 0.25 | 0 | 155791.7 | 5.983% | 6.816318 | 22.156% | 0.178937 | 2.139407 | 0.233571 | 0.868478 | 88.245% |
| 0.5 | 0 | 163881.8 | 11.486% | 6.367707 | 27.279% | 0.168338 | 1.916329 | 0.209417 | 0.864193 | 87.529% |
| 1 | 0 | 173624.6 | 18.114% | 3.627137 | 58.577% | 0.083633 | 1.259280 | 0.251528 | 0.817527 | 79.828% |
| 2 | 0 | 187649.6 | 27.655% | 2.958319 | 66.215% | 0.057999 | 1.062912 | 0.285788 | 0.796363 | 75.862% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

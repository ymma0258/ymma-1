# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.852208 | 0.000% | 0.281601 | 2.646365 | 0.161443 | 0.878704 | 90.379% |
| 0.5 | 0 | 148680.4 | 10.958% | 5.056976 | 42.873% | 0.149797 | 1.655797 | 0.217882 | 0.861601 | 86.234% |
| 1 | 0 | 158073.2 | 17.967% | 3.477191 | 60.720% | 0.091958 | 1.135270 | 0.282174 | 0.827169 | 80.221% |
| 1.5 | 0 | 165446.4 | 23.470% | 3.366420 | 61.971% | 0.089842 | 1.133632 | 0.312409 | 0.824750 | 79.848% |
| 2 | 0 | 172634.6 | 28.834% | 3.188499 | 63.981% | 0.081796 | 1.170049 | 0.336035 | 0.816199 | 78.363% |
| 3 | 0 | 185370.8 | 38.339% | 2.736373 | 69.088% | 0.059294 | 1.188573 | 0.368900 | 0.794402 | 74.810% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

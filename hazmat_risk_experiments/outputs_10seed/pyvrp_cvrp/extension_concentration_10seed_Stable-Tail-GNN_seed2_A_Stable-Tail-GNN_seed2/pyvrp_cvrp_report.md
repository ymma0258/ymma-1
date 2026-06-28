# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.852208 | 0.000% | 0.281601 | 2.646365 | 0.161443 | 0.878704 | 90.379% |
| 1 | 0 | 158073.2 | 17.967% | 3.477191 | 60.720% | 0.091958 | 1.135270 | 0.282174 | 0.827169 | 80.221% |
| 1 | 0.5 | 164095.1 | 22.461% | 3.276594 | 62.986% | 0.087055 | 1.101138 | 0.301832 | 0.818393 | 78.925% |
| 1 | 1 | 169889.6 | 26.786% | 3.200869 | 63.841% | 0.081887 | 1.145822 | 0.312085 | 0.814251 | 78.194% |
| 1 | 2 | 179712.5 | 34.116% | 2.725173 | 69.215% | 0.061457 | 1.190053 | 0.368878 | 0.792946 | 74.541% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

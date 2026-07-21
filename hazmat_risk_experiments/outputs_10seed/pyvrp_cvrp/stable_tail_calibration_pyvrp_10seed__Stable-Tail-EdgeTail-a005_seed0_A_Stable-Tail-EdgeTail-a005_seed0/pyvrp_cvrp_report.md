# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.6 | 0.000% | 7.682375 | 0.000% | 0.232759 | 2.463348 | 0.217734 | 0.884469 | 90.313% |
| 0.25 | 0 | 142404.2 | 6.168% | 4.570430 | 40.508% | 0.138680 | 1.627798 | 0.260015 | 0.861001 | 86.338% |
| 0.5 | 0 | 148189.4 | 10.481% | 3.833849 | 50.096% | 0.114316 | 1.464083 | 0.284518 | 0.843804 | 83.900% |
| 1 | 0 | 156127.3 | 16.399% | 2.354426 | 69.353% | 0.055026 | 0.952322 | 0.274300 | 0.774881 | 74.150% |
| 2 | 0 | 168555.9 | 25.665% | 1.719311 | 77.620% | 0.031368 | 0.575710 | 0.248386 | 0.722186 | 65.362% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

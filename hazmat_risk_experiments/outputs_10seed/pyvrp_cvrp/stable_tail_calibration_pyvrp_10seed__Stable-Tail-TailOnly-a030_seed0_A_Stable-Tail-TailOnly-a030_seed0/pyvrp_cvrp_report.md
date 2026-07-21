# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.2 | 0.000% | 7.785994 | 0.000% | 0.233078 | 2.435167 | 0.210666 | 0.885548 | 90.490% |
| 0.25 | 0 | 141673.0 | 5.728% | 4.617383 | 40.696% | 0.140248 | 1.476017 | 0.224434 | 0.861701 | 86.389% |
| 0.5 | 0 | 147081.9 | 9.764% | 3.820695 | 50.929% | 0.114409 | 1.591831 | 0.317218 | 0.843373 | 84.062% |
| 1 | 0 | 154747.7 | 15.485% | 2.573593 | 66.946% | 0.064432 | 0.936770 | 0.250435 | 0.788625 | 76.061% |
| 2 | 0 | 165807.7 | 23.739% | 1.842311 | 76.338% | 0.032772 | 0.617131 | 0.241463 | 0.734676 | 67.526% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

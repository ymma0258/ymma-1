# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 7.300744 | 0.000% | 0.229062 | 2.079228 | 0.158568 | 0.872470 | 88.827% |
| 0.25 | 0 | 142453.4 | 6.151% | 5.282757 | 27.641% | 0.147727 | 1.859656 | 0.265931 | 0.863377 | 86.853% |
| 0.5 | 0 | 148025.3 | 10.303% | 3.704879 | 49.253% | 0.108933 | 1.278001 | 0.269876 | 0.828536 | 81.836% |
| 1 | 0 | 155911.4 | 16.180% | 2.532777 | 65.308% | 0.066321 | 0.913111 | 0.248179 | 0.774482 | 73.849% |
| 2 | 0 | 167468.8 | 24.792% | 1.841560 | 74.776% | 0.039629 | 0.617415 | 0.246195 | 0.711497 | 64.813% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

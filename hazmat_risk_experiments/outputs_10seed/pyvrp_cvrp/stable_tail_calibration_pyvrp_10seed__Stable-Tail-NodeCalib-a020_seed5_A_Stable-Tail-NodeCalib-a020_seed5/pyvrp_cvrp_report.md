# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 7.320066 | 0.000% | 0.224205 | 2.074336 | 0.162948 | 0.873245 | 88.937% |
| 0.25 | 0 | 142417.1 | 6.230% | 5.087921 | 30.494% | 0.145462 | 1.604008 | 0.227805 | 0.859466 | 86.284% |
| 0.5 | 0 | 147843.1 | 10.278% | 3.726428 | 49.093% | 0.110674 | 1.398436 | 0.290506 | 0.830028 | 82.088% |
| 1 | 0 | 155805.9 | 16.217% | 2.511524 | 65.690% | 0.065017 | 0.991661 | 0.279074 | 0.772122 | 73.577% |
| 2 | 0 | 167389.6 | 24.857% | 1.863161 | 74.547% | 0.040050 | 0.616796 | 0.253762 | 0.712723 | 64.937% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

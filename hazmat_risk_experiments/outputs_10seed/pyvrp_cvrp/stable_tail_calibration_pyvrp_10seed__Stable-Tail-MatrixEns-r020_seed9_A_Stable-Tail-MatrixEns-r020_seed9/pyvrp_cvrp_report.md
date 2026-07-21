# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 6.794856 | 0.000% | 0.215947 | 1.939475 | 0.161211 | 0.870740 | 89.460% |
| 0.25 | 0 | 143088.7 | 6.784% | 4.714891 | 30.611% | 0.135119 | 1.590745 | 0.251127 | 0.858982 | 87.622% |
| 0.5 | 0 | 149429.1 | 11.516% | 3.540826 | 47.890% | 0.086011 | 1.335128 | 0.252650 | 0.831674 | 84.026% |
| 1 | 0 | 158266.7 | 18.111% | 2.389868 | 64.828% | 0.057244 | 0.800316 | 0.235724 | 0.778208 | 76.427% |
| 2 | 0 | 172136.4 | 28.462% | 2.032887 | 70.082% | 0.045806 | 0.607898 | 0.222772 | 0.754431 | 72.592% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

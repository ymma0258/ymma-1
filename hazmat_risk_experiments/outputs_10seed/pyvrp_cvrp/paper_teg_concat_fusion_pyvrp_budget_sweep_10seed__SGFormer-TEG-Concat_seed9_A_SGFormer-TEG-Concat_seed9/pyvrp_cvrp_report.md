# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.4 | 0.000% | 6.661897 | 0.000% | 0.212582 | 2.119767 | 0.226824 | 0.868185 | 87.279% |
| 0.25 | 0 | 140992.1 | 5.115% | 4.129038 | 38.020% | 0.103760 | 1.318013 | 0.211344 | 0.836689 | 81.353% |
| 0.5 | 0 | 145411.4 | 8.410% | 3.196938 | 52.012% | 0.076227 | 1.227780 | 0.244917 | 0.807337 | 76.822% |
| 1 | 0 | 152625.3 | 13.788% | 2.188300 | 67.152% | 0.047942 | 0.649259 | 0.159211 | 0.732110 | 66.188% |
| 2 | 0 | 163183.2 | 21.659% | 2.016201 | 69.735% | 0.043542 | 0.643186 | 0.211530 | 0.724627 | 64.427% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

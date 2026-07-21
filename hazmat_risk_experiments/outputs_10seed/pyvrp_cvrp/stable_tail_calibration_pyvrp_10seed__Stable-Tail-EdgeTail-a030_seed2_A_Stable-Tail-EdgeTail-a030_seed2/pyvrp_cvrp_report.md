# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 9.315639 | 0.000% | 0.303382 | 2.681804 | 0.171235 | 0.882943 | 90.593% |
| 0.25 | 0 | 142206.8 | 6.073% | 6.208891 | 33.350% | 0.182208 | 2.164829 | 0.273423 | 0.871321 | 88.349% |
| 0.5 | 0 | 148213.2 | 10.554% | 4.872678 | 47.694% | 0.145871 | 1.752262 | 0.258411 | 0.858624 | 85.904% |
| 1 | 0 | 157241.9 | 17.288% | 3.370566 | 63.818% | 0.094309 | 1.434745 | 0.350169 | 0.817986 | 79.855% |
| 2 | 0 | 171083.9 | 27.613% | 3.086267 | 66.870% | 0.079430 | 1.305869 | 0.328487 | 0.803678 | 77.603% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

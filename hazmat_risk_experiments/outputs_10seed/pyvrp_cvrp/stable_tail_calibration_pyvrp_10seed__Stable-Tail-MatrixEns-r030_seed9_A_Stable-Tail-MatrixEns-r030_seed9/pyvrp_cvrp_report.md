# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 5.990165 | 0.000% | 0.191813 | 1.700051 | 0.165006 | 0.872060 | 89.697% |
| 0.25 | 0 | 142998.8 | 6.664% | 4.016505 | 32.948% | 0.112956 | 1.278926 | 0.217449 | 0.856910 | 87.235% |
| 0.5 | 0 | 149239.0 | 11.319% | 3.035786 | 49.320% | 0.071694 | 1.207641 | 0.276367 | 0.827323 | 83.523% |
| 1 | 0 | 158008.4 | 17.860% | 1.991737 | 66.750% | 0.048231 | 0.642237 | 0.234358 | 0.772850 | 75.635% |
| 2 | 0 | 171799.5 | 28.147% | 1.681880 | 71.923% | 0.036892 | 0.486957 | 0.214623 | 0.742690 | 71.139% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

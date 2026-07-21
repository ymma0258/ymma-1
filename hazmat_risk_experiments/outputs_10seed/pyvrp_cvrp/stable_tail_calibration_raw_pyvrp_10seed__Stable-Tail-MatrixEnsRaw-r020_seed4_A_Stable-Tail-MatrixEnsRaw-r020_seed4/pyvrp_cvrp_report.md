# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.5 | 0.000% | 7.352197 | 0.000% | 0.230053 | 2.091157 | 0.169400 | 0.881340 | 90.464% |
| 0.25 | 0 | 143161.8 | 6.732% | 5.687797 | 22.638% | 0.178067 | 1.692040 | 0.198504 | 0.875622 | 89.400% |
| 0.5 | 0 | 150058.5 | 11.874% | 3.955913 | 46.194% | 0.118536 | 1.372045 | 0.272397 | 0.851278 | 85.369% |
| 1 | 0 | 159434.2 | 18.864% | 2.894052 | 60.637% | 0.073948 | 1.107504 | 0.332791 | 0.819333 | 80.492% |
| 2 | 0 | 174450.5 | 30.059% | 2.319274 | 68.455% | 0.054656 | 0.852032 | 0.328905 | 0.793766 | 76.450% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

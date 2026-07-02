# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 11.849915 | 0.000% | 0.302648 | 3.645547 | 0.184494 | 0.853949 | 88.811% |
| 1.5 | 1 | 211815.6 | 44.357% | 4.138947 | 65.072% | 0.076666 | 1.486324 | 0.318031 | 0.750878 | 73.488% |
| 2 | 1 | 220873.0 | 50.529% | 4.162366 | 64.874% | 0.076017 | 1.712859 | 0.375052 | 0.751027 | 73.384% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.185036 | 0.000% | 0.286891 | 3.021022 | 0.219674 | 0.881089 | 90.219% |
| 1 | 0 | 180557.0 | 23.053% | 3.982795 | 56.638% | 0.094027 | 1.540936 | 0.351918 | 0.837039 | 81.025% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

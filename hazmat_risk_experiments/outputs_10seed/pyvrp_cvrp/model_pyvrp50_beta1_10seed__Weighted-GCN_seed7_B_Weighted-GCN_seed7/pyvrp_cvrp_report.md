# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.427097 | 0.000% | 0.276640 | 2.927932 | 0.194858 | 0.842992 | 87.697% |
| 1 | 0 | 177040.8 | 20.657% | 4.154971 | 55.925% | 0.100094 | 1.310668 | 0.176102 | 0.748210 | 74.703% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

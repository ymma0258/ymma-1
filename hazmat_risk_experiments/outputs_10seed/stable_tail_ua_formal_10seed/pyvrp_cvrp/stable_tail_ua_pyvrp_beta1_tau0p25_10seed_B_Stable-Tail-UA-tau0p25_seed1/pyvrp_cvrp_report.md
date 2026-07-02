# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 14.779068 | 0.000% | 0.351935 | 4.665054 | 0.201339 | 0.850873 | 88.941% |
| 1 | 0 | 182268.3 | 24.219% | 6.844950 | 53.685% | 0.110547 | 2.414931 | 0.268382 | 0.796718 | 80.430% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

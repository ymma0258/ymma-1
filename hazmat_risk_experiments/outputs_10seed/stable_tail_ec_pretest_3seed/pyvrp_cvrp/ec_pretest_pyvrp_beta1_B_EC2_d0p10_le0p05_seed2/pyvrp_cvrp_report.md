# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.931694 | 0.000% | 0.297500 | 3.062123 | 0.188784 | 0.868465 | 90.448% |
| 1 | 0 | 181314.8 | 23.570% | 4.642830 | 53.252% | 0.122523 | 1.670341 | 0.298470 | 0.844144 | 84.187% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

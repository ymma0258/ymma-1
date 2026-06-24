# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.990982 | 0.000% | 0.247717 | 2.326027 | 0.146236 | 0.866164 | 89.323% |
| 1 | 0 | 160920.7 | 20.092% | 3.472697 | 56.542% | 0.080326 | 1.125769 | 0.257138 | 0.797910 | 79.107% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

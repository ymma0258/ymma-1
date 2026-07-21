# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 9.596571 | 0.000% | 0.317961 | 2.869005 | 0.166163 | 0.871984 | 89.493% |
| 0.25 | 0 | 141923.7 | 5.652% | 6.237641 | 35.001% | 0.188512 | 1.904767 | 0.203336 | 0.862057 | 87.413% |
| 0.5 | 0 | 147774.9 | 10.008% | 4.774720 | 50.246% | 0.119775 | 1.565257 | 0.217423 | 0.844914 | 84.282% |
| 1 | 0 | 156151.3 | 16.243% | 3.323529 | 65.368% | 0.073692 | 1.081637 | 0.230340 | 0.796861 | 77.404% |
| 2 | 0 | 168586.4 | 25.500% | 2.624720 | 72.649% | 0.053936 | 0.808125 | 0.232571 | 0.762343 | 72.096% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

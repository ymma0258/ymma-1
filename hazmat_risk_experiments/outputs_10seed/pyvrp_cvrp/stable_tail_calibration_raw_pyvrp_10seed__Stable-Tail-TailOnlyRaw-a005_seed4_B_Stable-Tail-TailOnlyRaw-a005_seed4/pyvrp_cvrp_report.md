# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.6 | 0.000% | 8.485842 | 0.000% | 0.265619 | 2.631511 | 0.185067 | 0.873757 | 89.132% |
| 0.25 | 0 | 157044.4 | 6.642% | 7.369676 | 13.153% | 0.212868 | 2.454749 | 0.240798 | 0.869449 | 88.208% |
| 0.5 | 0 | 165269.8 | 12.227% | 5.322010 | 37.284% | 0.144295 | 1.877653 | 0.292881 | 0.848647 | 84.560% |
| 1 | 0 | 175797.4 | 19.376% | 3.984732 | 53.043% | 0.102207 | 1.468622 | 0.278407 | 0.821274 | 80.315% |
| 2 | 0 | 191898.8 | 30.310% | 3.245230 | 61.757% | 0.070751 | 1.205130 | 0.273916 | 0.800834 | 76.875% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 9.116892 | 0.000% | 0.204100 | 2.853812 | 0.198262 | 0.876281 | 89.423% |
| 1 | 0 | 154038.8 | 14.956% | 2.774320 | 69.569% | 0.046040 | 0.951345 | 0.218775 | 0.754863 | 71.298% |
| 2 | 0 | 164319.6 | 22.629% | 2.240894 | 75.420% | 0.033035 | 0.692860 | 0.213792 | 0.715965 | 65.571% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

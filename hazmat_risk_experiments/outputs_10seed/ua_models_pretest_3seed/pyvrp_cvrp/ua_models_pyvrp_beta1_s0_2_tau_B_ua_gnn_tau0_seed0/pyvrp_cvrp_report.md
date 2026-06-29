# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 7.813180 | 0.000% | 0.213208 | 2.845630 | 0.257994 | 0.860039 | 89.354% |
| 1 | 0 | 180993.3 | 23.781% | 3.792095 | 51.465% | 0.081253 | 1.261897 | 0.262442 | 0.811786 | 81.069% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

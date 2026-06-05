# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 146665.2 | 0.000% | 7.713395 | 0.000% | 0.227294 | 2.685782 | 0.241826 | 0.847066 | 87.979% |
| 1 | 178727.4 | 21.861% | 3.617931 | 53.095% | 0.080911 | 1.268599 | 0.258479 | 0.763288 | 76.334% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

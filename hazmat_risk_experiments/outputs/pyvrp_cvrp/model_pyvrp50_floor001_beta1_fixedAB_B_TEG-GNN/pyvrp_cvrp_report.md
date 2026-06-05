# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 146531.2 | 0.000% | 8.199420 | 0.000% | 0.236188 | 2.653961 | 0.209952 | 0.838219 | 86.846% |
| 1 | 178390.8 | 21.743% | 3.891981 | 52.533% | 0.076918 | 1.287324 | 0.236042 | 0.724841 | 72.631% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

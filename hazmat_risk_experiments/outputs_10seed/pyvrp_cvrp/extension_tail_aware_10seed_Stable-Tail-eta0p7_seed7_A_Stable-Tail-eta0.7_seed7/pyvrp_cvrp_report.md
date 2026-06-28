# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 12.161875 | 0.000% | 0.222645 | 3.427581 | 0.144326 | 0.871982 | 89.609% |
| 1 | 0 | 159631.6 | 19.130% | 3.828229 | 68.523% | 0.046773 | 1.198786 | 0.269583 | 0.778815 | 73.385% |
| 2 | 0 | 172718.8 | 28.897% | 3.355154 | 72.413% | 0.037950 | 1.275959 | 0.303291 | 0.747699 | 68.915% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

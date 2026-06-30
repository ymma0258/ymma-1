# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 8.493492 | 0.000% | 0.256297 | 3.064367 | 0.283512 | 0.880119 | 90.245% |
| 1 | 0 | 178382.7 | 21.996% | 4.053968 | 52.270% | 0.097405 | 1.793874 | 0.383867 | 0.842680 | 82.518% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

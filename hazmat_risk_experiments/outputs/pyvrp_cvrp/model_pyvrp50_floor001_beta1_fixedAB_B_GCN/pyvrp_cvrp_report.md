# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 146531.2 | 0.000% | 7.712965 | 0.000% | 0.232754 | 2.675041 | 0.252832 | 0.859204 | 89.101% |
| 1 | 179227.6 | 22.314% | 3.678792 | 52.304% | 0.091462 | 1.321969 | 0.329059 | 0.813603 | 80.999% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

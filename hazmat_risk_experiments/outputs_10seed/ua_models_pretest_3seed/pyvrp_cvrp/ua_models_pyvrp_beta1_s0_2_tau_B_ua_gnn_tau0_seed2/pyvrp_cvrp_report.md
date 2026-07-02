# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 7.481353 | 0.000% | 0.228482 | 2.819084 | 0.288007 | 0.858712 | 89.745% |
| 1 | 0 | 179935.7 | 23.058% | 4.123193 | 44.887% | 0.087479 | 1.382910 | 0.250694 | 0.818002 | 82.923% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

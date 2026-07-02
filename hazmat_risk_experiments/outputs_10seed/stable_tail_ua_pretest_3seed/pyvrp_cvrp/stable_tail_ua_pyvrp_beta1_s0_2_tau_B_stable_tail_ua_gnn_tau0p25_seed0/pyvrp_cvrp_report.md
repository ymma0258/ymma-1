# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 11.334605 | 0.000% | 0.217139 | 3.857712 | 0.225843 | 0.855345 | 89.302% |
| 1 | 0 | 181001.3 | 23.786% | 5.549099 | 51.043% | 0.115412 | 1.920141 | 0.300123 | 0.795943 | 80.613% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

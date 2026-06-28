# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.519431 | 0.000% | 0.251641 | 2.779042 | 0.217431 | 0.841806 | 87.151% |
| 1 | 0 | 177482.7 | 20.958% | 4.207384 | 50.614% | 0.104438 | 1.659465 | 0.335011 | 0.758786 | 75.875% |
| 1 | 1 | 192099.1 | 30.919% | 3.342797 | 60.763% | 0.061390 | 1.359783 | 0.312751 | 0.705654 | 68.975% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

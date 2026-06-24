# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.415948 | 0.000% | 0.258554 | 2.427981 | 0.138699 | 0.853103 | 88.461% |
| 1 | 0 | 161895.3 | 20.820% | 3.571949 | 57.557% | 0.079373 | 1.252764 | 0.307868 | 0.772329 | 76.856% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

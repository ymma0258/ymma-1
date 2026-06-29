# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.851676 | 0.000% | 0.287040 | 3.185509 | 0.204509 | 0.879458 | 90.687% |
| 2 | 2 | 223633.7 | 52.411% | 2.974279 | 69.809% | 0.065841 | 1.107225 | 0.332780 | 0.794764 | 74.118% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

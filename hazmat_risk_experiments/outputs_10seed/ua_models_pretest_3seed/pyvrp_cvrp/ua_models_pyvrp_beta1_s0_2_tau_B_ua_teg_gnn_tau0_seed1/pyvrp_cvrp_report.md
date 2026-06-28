# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 8.947346 | 0.000% | 0.273034 | 3.058313 | 0.239255 | 0.871928 | 90.587% |
| 1 | 0 | 177731.3 | 21.550% | 4.232865 | 52.691% | 0.088659 | 1.506403 | 0.294788 | 0.832376 | 82.680% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

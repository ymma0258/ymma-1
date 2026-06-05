# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 7.494949 | 0.000% | 0.243196 | 2.334200 | 0.184260 | 0.831644 | 85.831% |
| 1 | 0 | 157331.2 | 17.414% | 3.011532 | 59.819% | 0.060644 | 1.068477 | 0.272558 | 0.685888 | 67.850% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

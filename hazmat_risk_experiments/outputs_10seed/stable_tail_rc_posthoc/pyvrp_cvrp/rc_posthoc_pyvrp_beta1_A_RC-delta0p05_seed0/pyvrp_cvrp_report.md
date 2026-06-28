# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 8.392596 | 0.000% | 0.266790 | 2.530357 | 0.202916 | 0.882982 | 90.534% |
| 1 | 0 | 157004.2 | 17.111% | 2.525945 | 69.903% | 0.054192 | 0.994724 | 0.298520 | 0.792575 | 75.828% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

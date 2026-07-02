# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 8.134302 | 0.000% | 0.235037 | 2.902500 | 0.274128 | 0.887179 | 90.322% |
| 1 | 0 | 173230.0 | 18.472% | 3.338464 | 58.958% | 0.080680 | 1.034447 | 0.230032 | 0.822354 | 78.543% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

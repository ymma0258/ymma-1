# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.839842 | 0.000% | 0.274851 | 2.527199 | 0.141563 | 0.874007 | 89.930% |
| 1 | 0 | 160225.5 | 19.573% | 3.516444 | 60.221% | 0.076175 | 1.302529 | 0.325948 | 0.810319 | 78.943% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

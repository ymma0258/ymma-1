# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 11.883079 | 0.000% | 0.316278 | 3.678860 | 0.189477 | 0.849482 | 87.857% |
| 1.5 | 1 | 219544.6 | 49.488% | 4.693248 | 60.505% | 0.087503 | 1.833352 | 0.351266 | 0.768153 | 75.498% |
| 2 | 1 | 230501.2 | 56.949% | 4.680374 | 60.613% | 0.089680 | 1.791038 | 0.387422 | 0.769195 | 75.608% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

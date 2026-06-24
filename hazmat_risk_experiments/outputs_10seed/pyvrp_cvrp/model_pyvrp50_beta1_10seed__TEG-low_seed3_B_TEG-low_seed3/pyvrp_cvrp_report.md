# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.849915 | 0.000% | 0.235421 | 2.458468 | 0.193165 | 0.829028 | 86.144% |
| 1 | 0 | 177595.1 | 21.035% | 3.642575 | 53.597% | 0.083894 | 1.045124 | 0.200044 | 0.719488 | 72.036% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

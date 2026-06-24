# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.334046 | 0.000% | 0.259283 | 2.992092 | 0.204568 | 0.848910 | 88.601% |
| 1 | 0 | 179192.2 | 22.123% | 4.432396 | 52.514% | 0.114274 | 1.497336 | 0.238688 | 0.784213 | 78.826% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 6.893167 | 0.000% | 0.199200 | 2.246605 | 0.216485 | 0.871658 | 88.743% |
| 1 | 0 | 174572.6 | 18.813% | 3.012381 | 56.299% | 0.075235 | 1.139610 | 0.291646 | 0.806665 | 78.252% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

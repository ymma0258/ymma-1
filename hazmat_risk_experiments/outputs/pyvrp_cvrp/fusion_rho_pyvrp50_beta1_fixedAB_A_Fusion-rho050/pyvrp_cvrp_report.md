# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 133997.4 | 0.000% | 7.387750 | 0.000% | 0.211587 | 2.454359 | 0.219332 | 0.850049 | 87.832% |
| 1 | 158509.6 | 18.293% | 2.806267 | 62.015% | 0.065694 | 0.952488 | 0.266217 | 0.731482 | 72.305% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

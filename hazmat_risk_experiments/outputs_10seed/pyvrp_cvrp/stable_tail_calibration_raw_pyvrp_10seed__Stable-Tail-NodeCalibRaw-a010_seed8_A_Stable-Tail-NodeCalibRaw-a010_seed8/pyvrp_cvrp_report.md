# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.9 | 0.000% | 8.231298 | 0.000% | 0.258793 | 2.445829 | 0.185766 | 0.870660 | 88.808% |
| 0.25 | 0 | 143126.4 | 6.600% | 5.690474 | 30.868% | 0.164261 | 1.782745 | 0.228349 | 0.860185 | 87.325% |
| 0.5 | 0 | 149978.2 | 11.703% | 3.876587 | 52.904% | 0.112137 | 1.267084 | 0.204724 | 0.825623 | 81.943% |
| 1 | 0 | 158726.9 | 18.219% | 2.793722 | 66.060% | 0.062730 | 0.775006 | 0.164356 | 0.780979 | 75.552% |
| 2 | 0 | 173643.5 | 29.329% | 2.325238 | 71.751% | 0.045741 | 0.778653 | 0.250739 | 0.750473 | 70.734% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

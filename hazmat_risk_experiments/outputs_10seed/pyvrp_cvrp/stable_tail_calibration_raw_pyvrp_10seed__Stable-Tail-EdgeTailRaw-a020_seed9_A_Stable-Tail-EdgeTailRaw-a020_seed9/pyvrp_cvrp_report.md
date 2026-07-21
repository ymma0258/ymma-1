# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134531.0 | 0.000% | 9.151900 | 0.000% | 0.298613 | 2.602444 | 0.165406 | 0.871164 | 89.222% |
| 0.25 | 0 | 143119.6 | 6.384% | 5.545456 | 39.406% | 0.158766 | 1.853598 | 0.240584 | 0.853840 | 86.882% |
| 0.5 | 0 | 149202.7 | 10.906% | 4.520267 | 50.608% | 0.125377 | 1.769107 | 0.272530 | 0.833351 | 84.126% |
| 1 | 0 | 158156.2 | 17.561% | 3.076342 | 66.386% | 0.074974 | 1.092915 | 0.260035 | 0.783961 | 77.127% |
| 2 | 0 | 172132.9 | 27.950% | 2.502497 | 72.656% | 0.053301 | 0.734574 | 0.197885 | 0.752635 | 72.362% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

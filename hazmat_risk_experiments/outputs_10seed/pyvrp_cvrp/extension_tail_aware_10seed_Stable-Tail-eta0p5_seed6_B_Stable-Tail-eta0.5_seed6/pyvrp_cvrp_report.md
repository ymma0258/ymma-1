# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 11.992339 | 0.000% | 0.278158 | 3.978234 | 0.229188 | 0.883737 | 90.357% |
| 1 | 0 | 180274.1 | 22.860% | 5.022202 | 58.122% | 0.068795 | 2.009091 | 0.374943 | 0.842097 | 80.762% |
| 2 | 0 | 201009.9 | 36.992% | 4.704882 | 60.768% | 0.063747 | 2.016118 | 0.382016 | 0.831418 | 79.102% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

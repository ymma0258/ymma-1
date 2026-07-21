# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.6 | 0.000% | 7.935472 | 0.000% | 0.236579 | 2.263924 | 0.160171 | 0.867384 | 88.816% |
| 0.25 | 0 | 143161.4 | 6.732% | 5.234639 | 34.035% | 0.149197 | 1.735311 | 0.274354 | 0.847833 | 85.539% |
| 0.5 | 0 | 149295.3 | 11.305% | 4.108754 | 48.223% | 0.121133 | 1.634423 | 0.328989 | 0.821343 | 82.255% |
| 1 | 0 | 158803.5 | 18.394% | 2.829221 | 64.347% | 0.075560 | 0.940470 | 0.289713 | 0.773286 | 75.223% |
| 2 | 0 | 173436.3 | 29.303% | 2.283140 | 71.229% | 0.052837 | 0.821696 | 0.294496 | 0.731129 | 69.296% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

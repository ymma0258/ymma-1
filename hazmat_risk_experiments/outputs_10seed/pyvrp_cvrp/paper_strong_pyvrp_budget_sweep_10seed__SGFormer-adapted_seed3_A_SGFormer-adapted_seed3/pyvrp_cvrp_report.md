# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.9 | 0.000% | 6.121727 | 0.000% | 0.184847 | 1.976396 | 0.227280 | 0.860034 | 86.073% |
| 0.25 | 0 | 140898.0 | 4.940% | 3.669894 | 40.051% | 0.092179 | 1.242310 | 0.246199 | 0.823131 | 79.229% |
| 0.5 | 0 | 144433.7 | 7.574% | 2.508037 | 59.031% | 0.057383 | 0.772259 | 0.188680 | 0.769447 | 71.310% |
| 1 | 0 | 151915.1 | 13.146% | 2.265331 | 62.995% | 0.050017 | 0.674653 | 0.198985 | 0.751082 | 68.083% |
| 2 | 0 | 162256.6 | 20.848% | 1.676618 | 72.612% | 0.029930 | 0.520180 | 0.204073 | 0.670859 | 56.636% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

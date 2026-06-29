# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 10.484908 | 0.000% | 0.255078 | 3.034653 | 0.152398 | 0.852508 | 88.503% |
| 1.5 | 1 | 184419.0 | 37.629% | 3.083033 | 70.596% | 0.053542 | 1.319161 | 0.328861 | 0.686353 | 66.329% |
| 2 | 1 | 191044.5 | 42.573% | 3.003125 | 71.358% | 0.052106 | 1.325017 | 0.343472 | 0.679152 | 65.447% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.7 | 0.000% | 5.462846 | 0.000% | 0.172936 | 1.616691 | 0.171117 | 0.849999 | 89.011% |
| 0.25 | 0 | 159060.0 | 8.108% | 4.635359 | 15.148% | 0.145505 | 1.511501 | 0.229530 | 0.845748 | 88.841% |
| 0.5 | 0 | 169563.4 | 15.247% | 3.739884 | 31.540% | 0.105190 | 1.185016 | 0.218404 | 0.838982 | 86.785% |
| 1 | 0 | 184357.9 | 25.302% | 2.742282 | 49.801% | 0.071335 | 0.944051 | 0.270124 | 0.811204 | 82.200% |
| 2 | 0 | 206149.9 | 40.113% | 2.221040 | 59.343% | 0.053425 | 0.820645 | 0.338329 | 0.783110 | 77.916% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 9.086866 | 0.000% | 0.217123 | 2.818483 | 0.164488 | 0.886678 | 90.323% |
| 1 | 0 | 158093.4 | 17.982% | 3.491958 | 61.571% | 0.073832 | 1.098122 | 0.241874 | 0.823380 | 79.445% |
| 2 | 0 | 172184.4 | 28.498% | 2.773776 | 69.475% | 0.053606 | 1.122818 | 0.329285 | 0.796028 | 74.648% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 8.536087 | 0.000% | 0.272584 | 2.604070 | 0.194369 | 0.882200 | 90.339% |
| 0.25 | 0 | 141375.5 | 5.296% | 6.225114 | 27.073% | 0.195588 | 1.903045 | 0.196784 | 0.879140 | 88.949% |
| 0.5 | 0 | 146929.3 | 9.432% | 4.928723 | 42.260% | 0.156490 | 1.763551 | 0.243995 | 0.866811 | 86.491% |
| 1 | 0 | 155626.1 | 15.910% | 3.171627 | 62.844% | 0.085550 | 1.234191 | 0.277935 | 0.821756 | 79.411% |
| 2 | 0 | 167311.3 | 24.613% | 2.387271 | 72.033% | 0.057575 | 1.015438 | 0.303994 | 0.785360 | 73.033% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

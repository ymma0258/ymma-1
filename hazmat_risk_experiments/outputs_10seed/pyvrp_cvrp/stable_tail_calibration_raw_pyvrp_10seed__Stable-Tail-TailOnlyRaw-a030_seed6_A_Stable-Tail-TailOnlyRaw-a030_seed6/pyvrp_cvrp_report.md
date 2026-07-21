# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.1 | 0.000% | 9.333021 | 0.000% | 0.285930 | 2.677576 | 0.161088 | 0.877636 | 90.284% |
| 0.25 | 0 | 143530.3 | 6.954% | 5.295110 | 43.265% | 0.157098 | 1.727641 | 0.252092 | 0.850883 | 85.957% |
| 0.5 | 0 | 149658.5 | 11.521% | 4.552392 | 51.223% | 0.139072 | 1.772815 | 0.318286 | 0.835894 | 83.785% |
| 1 | 0 | 158871.8 | 18.386% | 3.161569 | 66.125% | 0.086186 | 1.107958 | 0.312685 | 0.794323 | 77.666% |
| 2 | 0 | 172887.1 | 28.830% | 2.442800 | 73.826% | 0.058341 | 0.972406 | 0.332422 | 0.747596 | 71.302% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

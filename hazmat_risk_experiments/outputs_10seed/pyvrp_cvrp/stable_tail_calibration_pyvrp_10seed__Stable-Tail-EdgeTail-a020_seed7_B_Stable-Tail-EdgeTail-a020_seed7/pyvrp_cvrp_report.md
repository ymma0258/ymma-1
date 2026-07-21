# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 10.351661 | 0.000% | 0.313210 | 3.123761 | 0.181032 | 0.879906 | 90.823% |
| 0.25 | 0 | 157803.9 | 7.449% | 7.841454 | 24.249% | 0.218165 | 2.488415 | 0.229981 | 0.875352 | 89.069% |
| 0.5 | 0 | 167050.2 | 13.745% | 5.850304 | 43.484% | 0.161141 | 2.187143 | 0.295105 | 0.856577 | 85.474% |
| 1 | 0 | 178372.6 | 21.454% | 3.837961 | 62.924% | 0.091811 | 1.244204 | 0.217847 | 0.823110 | 79.642% |
| 2 | 0 | 195115.5 | 32.855% | 3.351439 | 67.624% | 0.070749 | 1.070386 | 0.231579 | 0.811820 | 77.562% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

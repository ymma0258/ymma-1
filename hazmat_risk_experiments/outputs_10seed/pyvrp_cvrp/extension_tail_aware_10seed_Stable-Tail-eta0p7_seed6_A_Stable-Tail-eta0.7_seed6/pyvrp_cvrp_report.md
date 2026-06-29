# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 10.780756 | 0.000% | 0.188860 | 3.170030 | 0.162189 | 0.878803 | 89.457% |
| 1 | 0 | 160587.9 | 19.844% | 3.464895 | 67.860% | 0.039106 | 1.322393 | 0.321899 | 0.778378 | 73.246% |
| 2 | 0 | 175175.0 | 30.730% | 3.178239 | 70.519% | 0.035680 | 1.308739 | 0.327157 | 0.766125 | 71.498% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

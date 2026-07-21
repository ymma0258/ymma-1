# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 6.199408 | 0.000% | 0.177818 | 1.821627 | 0.167485 | 0.872048 | 88.968% |
| 0.25 | 0 | 141810.7 | 5.778% | 4.316627 | 30.370% | 0.123540 | 1.287244 | 0.188453 | 0.855417 | 86.544% |
| 0.5 | 0 | 147185.8 | 9.787% | 3.230388 | 47.892% | 0.094002 | 1.181244 | 0.259025 | 0.832325 | 83.025% |
| 1 | 0 | 155235.5 | 15.792% | 2.033527 | 67.198% | 0.051517 | 0.647532 | 0.255567 | 0.761217 | 72.927% |
| 2 | 0 | 167534.6 | 24.966% | 1.889091 | 69.528% | 0.045097 | 0.660333 | 0.269077 | 0.750819 | 71.233% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

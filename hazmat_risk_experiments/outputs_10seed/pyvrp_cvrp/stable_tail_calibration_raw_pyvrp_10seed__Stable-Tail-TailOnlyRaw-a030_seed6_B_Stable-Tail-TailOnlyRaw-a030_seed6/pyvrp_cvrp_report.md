# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.7 | 0.000% | 10.280327 | 0.000% | 0.306286 | 3.379275 | 0.225458 | 0.878767 | 90.694% |
| 0.25 | 0 | 158280.7 | 7.676% | 9.062703 | 11.844% | 0.231196 | 3.065147 | 0.255497 | 0.879326 | 90.643% |
| 0.5 | 0 | 168415.8 | 14.570% | 7.070819 | 31.220% | 0.183201 | 2.531290 | 0.269756 | 0.870599 | 88.443% |
| 1 | 0 | 181920.2 | 23.757% | 4.591266 | 55.339% | 0.122256 | 1.798679 | 0.357161 | 0.843906 | 83.028% |
| 2 | 0 | 202844.1 | 37.991% | 4.287708 | 58.292% | 0.112848 | 1.747301 | 0.370866 | 0.839063 | 81.997% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

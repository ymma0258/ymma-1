# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 8.745877 | 0.000% | 0.261673 | 2.944427 | 0.263191 | 0.875231 | 90.023% |
| 0.25 | 0 | 158294.8 | 7.491% | 7.728936 | 11.628% | 0.209311 | 2.565910 | 0.255836 | 0.874581 | 89.334% |
| 0.5 | 0 | 168567.9 | 14.467% | 6.119188 | 30.033% | 0.162497 | 1.769415 | 0.187223 | 0.859710 | 86.616% |
| 1 | 0 | 183501.6 | 24.607% | 4.451880 | 49.097% | 0.104949 | 1.673808 | 0.300730 | 0.838136 | 82.511% |
| 2 | 0 | 207048.6 | 40.597% | 3.845581 | 56.030% | 0.081047 | 1.288511 | 0.266228 | 0.826077 | 79.910% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

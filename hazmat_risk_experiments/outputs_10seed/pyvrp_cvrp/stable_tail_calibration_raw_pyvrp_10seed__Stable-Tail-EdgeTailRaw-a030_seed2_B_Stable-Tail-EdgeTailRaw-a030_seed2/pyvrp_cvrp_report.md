# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.0 | 0.000% | 9.669148 | 0.000% | 0.306796 | 3.586871 | 0.315736 | 0.880870 | 90.393% |
| 0.25 | 0 | 156741.3 | 6.436% | 7.919192 | 18.098% | 0.242505 | 2.850662 | 0.321236 | 0.877645 | 89.509% |
| 0.5 | 0 | 165090.3 | 12.105% | 6.180967 | 36.075% | 0.168290 | 2.336712 | 0.270423 | 0.864141 | 87.139% |
| 1 | 0 | 177592.2 | 20.594% | 4.875814 | 49.573% | 0.130069 | 2.009738 | 0.296740 | 0.851568 | 84.423% |
| 2 | 0 | 196274.0 | 33.280% | 3.714072 | 61.588% | 0.093189 | 1.873198 | 0.385261 | 0.829255 | 80.291% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

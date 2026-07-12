# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 9.369218 | 0.000% | 0.285758 | 2.610212 | 0.144500 | 0.881047 | 88.913% |
| 0.25 | 0 | 156933.7 | 6.760% | 7.571533 | 19.187% | 0.226284 | 2.255374 | 0.225398 | 0.874624 | 87.489% |
| 0.5 | 0 | 165357.9 | 12.490% | 4.709674 | 49.732% | 0.126923 | 1.451937 | 0.226258 | 0.837160 | 81.127% |
| 1 | 0 | 175691.7 | 19.520% | 3.322885 | 64.534% | 0.076787 | 1.031228 | 0.209098 | 0.790355 | 73.296% |
| 2 | 0 | 190451.8 | 29.561% | 2.725896 | 70.906% | 0.053405 | 0.897729 | 0.253501 | 0.764226 | 68.585% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

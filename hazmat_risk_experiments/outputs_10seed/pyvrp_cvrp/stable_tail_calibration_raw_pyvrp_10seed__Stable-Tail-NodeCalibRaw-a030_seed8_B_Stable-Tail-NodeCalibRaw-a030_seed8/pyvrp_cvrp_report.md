# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 7.585632 | 0.000% | 0.210075 | 2.264989 | 0.184911 | 0.859849 | 87.770% |
| 0.25 | 0 | 156748.2 | 6.537% | 6.436337 | 15.151% | 0.154311 | 2.111838 | 0.227605 | 0.854717 | 87.014% |
| 0.5 | 0 | 165305.2 | 12.353% | 4.980801 | 34.339% | 0.125340 | 1.657197 | 0.247255 | 0.840030 | 83.967% |
| 1 | 0 | 176194.8 | 19.754% | 3.054307 | 59.736% | 0.070056 | 1.111472 | 0.256362 | 0.782578 | 75.390% |
| 2 | 0 | 190999.9 | 29.817% | 2.516021 | 66.832% | 0.049845 | 0.745609 | 0.210295 | 0.755075 | 70.868% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

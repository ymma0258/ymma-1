# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.9 | 0.000% | 9.138202 | 0.000% | 0.288322 | 2.766155 | 0.177526 | 0.861613 | 88.990% |
| 0.25 | 0 | 143799.8 | 7.102% | 7.147306 | 21.787% | 0.206796 | 1.966630 | 0.126736 | 0.855746 | 88.595% |
| 0.5 | 0 | 151172.7 | 12.593% | 4.893140 | 46.454% | 0.147157 | 1.609557 | 0.226949 | 0.828138 | 84.053% |
| 1 | 0 | 161482.4 | 20.271% | 3.442985 | 62.323% | 0.085315 | 1.240227 | 0.295038 | 0.777555 | 77.134% |
| 2 | 0 | 177586.6 | 32.266% | 2.678529 | 70.689% | 0.049846 | 0.931046 | 0.256980 | 0.726869 | 70.322% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

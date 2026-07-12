# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.7 | 0.000% | 9.004547 | 0.000% | 0.289405 | 2.521692 | 0.154719 | 0.854907 | 88.627% |
| 0.25 | 0 | 144109.7 | 7.333% | 6.367184 | 29.289% | 0.174886 | 2.064819 | 0.237223 | 0.842610 | 87.215% |
| 0.5 | 0 | 151121.5 | 12.555% | 4.823902 | 46.428% | 0.139748 | 1.518208 | 0.196383 | 0.815150 | 83.357% |
| 1 | 0 | 162091.2 | 20.725% | 3.336546 | 62.946% | 0.085453 | 1.146287 | 0.281833 | 0.761997 | 75.924% |
| 2 | 0 | 178414.5 | 32.883% | 2.557517 | 71.597% | 0.047945 | 0.881535 | 0.284608 | 0.699254 | 67.894% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

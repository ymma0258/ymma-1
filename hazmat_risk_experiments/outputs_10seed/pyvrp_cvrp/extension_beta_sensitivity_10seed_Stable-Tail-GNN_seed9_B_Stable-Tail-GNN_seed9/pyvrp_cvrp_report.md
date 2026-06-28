# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.896748 | 0.000% | 0.226106 | 2.693672 | 0.247272 | 0.880410 | 90.324% |
| 0.5 | 0 | 163925.9 | 11.719% | 4.676578 | 40.778% | 0.122110 | 1.539348 | 0.245288 | 0.856339 | 84.963% |
| 1 | 0 | 172393.9 | 17.490% | 2.521559 | 68.068% | 0.052392 | 0.884797 | 0.275269 | 0.786921 | 74.256% |
| 1.5 | 0 | 178016.5 | 21.322% | 2.117162 | 73.189% | 0.042472 | 0.704891 | 0.230528 | 0.756019 | 69.805% |
| 2 | 0 | 183744.2 | 25.225% | 2.145795 | 72.827% | 0.042291 | 0.761580 | 0.244510 | 0.753096 | 69.564% |
| 3 | 0 | 194818.5 | 32.773% | 2.045724 | 74.094% | 0.039821 | 0.743622 | 0.252407 | 0.750029 | 68.570% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.7 | 0.000% | 7.965389 | 0.000% | 0.241295 | 2.471588 | 0.211106 | 0.864249 | 88.239% |
| 0.25 | 0 | 156300.2 | 6.232% | 6.504303 | 18.343% | 0.160974 | 2.041196 | 0.203624 | 0.857603 | 87.213% |
| 0.5 | 0 | 164864.1 | 12.053% | 5.027547 | 36.883% | 0.122008 | 1.632421 | 0.207697 | 0.840552 | 84.316% |
| 1 | 0 | 175105.5 | 19.014% | 3.291094 | 58.683% | 0.080486 | 1.029191 | 0.206275 | 0.791926 | 77.062% |
| 2 | 0 | 189496.2 | 28.794% | 2.481494 | 68.847% | 0.055270 | 0.736704 | 0.214130 | 0.754359 | 70.807% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.3 | 0.000% | 4.721104 | 0.000% | 0.125648 | 1.587075 | 0.257387 | 0.880833 | 90.020% |
| 0.25 | 0 | 156495.7 | 6.317% | 3.949071 | 16.353% | 0.097181 | 1.330168 | 0.231467 | 0.875111 | 88.842% |
| 0.5 | 0 | 164476.2 | 11.739% | 2.766823 | 41.395% | 0.070770 | 0.997013 | 0.236086 | 0.851945 | 84.773% |
| 1 | 0 | 174961.6 | 18.862% | 1.909560 | 59.553% | 0.047853 | 0.713903 | 0.296835 | 0.812389 | 78.581% |
| 2 | 0 | 189951.6 | 29.046% | 1.535650 | 67.473% | 0.032568 | 0.606568 | 0.296198 | 0.790853 | 74.395% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

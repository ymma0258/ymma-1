# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 8.738093 | 0.000% | 0.298642 | 2.851042 | 0.217802 | 0.876264 | 88.550% |
| 0.25 | 0 | 143769.2 | 7.292% | 5.172344 | 40.807% | 0.151347 | 2.174747 | 0.318362 | 0.845042 | 82.634% |
| 0.5 | 0 | 150144.0 | 12.049% | 3.783969 | 56.696% | 0.099987 | 1.583685 | 0.301042 | 0.804458 | 76.334% |
| 1 | 0 | 157876.1 | 17.820% | 2.478641 | 71.634% | 0.053422 | 0.792994 | 0.229857 | 0.731610 | 65.610% |
| 2 | 0 | 169637.2 | 26.597% | 2.112387 | 75.826% | 0.040679 | 0.623326 | 0.196279 | 0.701873 | 61.050% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 9.004532 | 0.000% | 0.272283 | 2.770961 | 0.172556 | 0.865861 | 88.680% |
| 0.25 | 0 | 157594.8 | 7.209% | 7.830441 | 13.039% | 0.192394 | 2.439491 | 0.197060 | 0.865849 | 89.269% |
| 0.5 | 0 | 167576.3 | 14.000% | 6.205870 | 31.081% | 0.159834 | 2.110962 | 0.274184 | 0.852790 | 86.859% |
| 1 | 0 | 182463.8 | 24.127% | 4.865070 | 45.971% | 0.127662 | 1.772078 | 0.330115 | 0.835789 | 83.490% |
| 2 | 0 | 205932.7 | 40.093% | 4.092740 | 54.548% | 0.106806 | 1.453536 | 0.324685 | 0.825254 | 80.708% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

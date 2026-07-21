# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.9 | 0.000% | 7.536248 | 0.000% | 0.227813 | 2.357408 | 0.204389 | 0.859792 | 87.781% |
| 0.25 | 0 | 156687.8 | 6.399% | 6.330923 | 15.994% | 0.153185 | 1.991884 | 0.192205 | 0.856525 | 87.069% |
| 0.5 | 0 | 165558.3 | 12.423% | 4.781681 | 36.551% | 0.116128 | 1.468976 | 0.210751 | 0.833385 | 83.332% |
| 1 | 0 | 176656.9 | 19.959% | 3.208315 | 57.428% | 0.077885 | 1.171165 | 0.250416 | 0.787259 | 76.311% |
| 2 | 0 | 191586.6 | 30.097% | 2.478856 | 67.108% | 0.053983 | 0.760425 | 0.218254 | 0.754641 | 70.939% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

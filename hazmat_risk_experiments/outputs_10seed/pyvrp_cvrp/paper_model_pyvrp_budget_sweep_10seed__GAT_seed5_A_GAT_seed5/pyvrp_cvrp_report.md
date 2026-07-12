# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.6 | 0.000% | 7.373494 | 0.000% | 0.234380 | 2.146232 | 0.150733 | 0.876907 | 90.400% |
| 0.25 | 0 | 142815.2 | 6.210% | 4.870033 | 33.952% | 0.159430 | 1.517897 | 0.221472 | 0.871037 | 88.042% |
| 0.5 | 0 | 149112.7 | 10.894% | 4.110894 | 44.248% | 0.130302 | 1.189713 | 0.192440 | 0.862236 | 86.283% |
| 1 | 0 | 159511.2 | 18.627% | 3.018470 | 59.063% | 0.089051 | 0.967626 | 0.227632 | 0.838963 | 81.748% |
| 2 | 0 | 175734.9 | 30.692% | 2.684956 | 63.586% | 0.073048 | 0.994713 | 0.292285 | 0.824242 | 79.303% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

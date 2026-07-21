# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.7 | 0.000% | 9.326836 | 0.000% | 0.310240 | 2.576636 | 0.155431 | 0.870989 | 88.920% |
| 0.25 | 0 | 143549.7 | 6.756% | 5.866470 | 37.101% | 0.168235 | 1.821034 | 0.210541 | 0.854588 | 86.301% |
| 0.5 | 0 | 149398.7 | 11.106% | 4.685902 | 49.759% | 0.135918 | 1.922472 | 0.286485 | 0.838015 | 83.638% |
| 1 | 0 | 158852.2 | 18.137% | 3.255015 | 65.101% | 0.088341 | 1.278042 | 0.305515 | 0.794390 | 76.748% |
| 2 | 0 | 172243.0 | 28.095% | 2.592142 | 72.208% | 0.059276 | 0.882188 | 0.266102 | 0.761205 | 71.439% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

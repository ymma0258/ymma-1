# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.252978 | 0.000% | 0.228850 | 2.342966 | 0.200924 | 0.879225 | 89.845% |
| 0.5 | 0 | 147106.9 | 9.783% | 3.706090 | 48.903% | 0.086215 | 1.541035 | 0.301149 | 0.838164 | 83.532% |
| 1 | 0 | 154374.9 | 15.207% | 2.292019 | 68.399% | 0.046838 | 0.707972 | 0.170744 | 0.760009 | 72.492% |
| 1.5 | 0 | 159977.4 | 19.388% | 2.171642 | 70.059% | 0.044511 | 0.744689 | 0.219961 | 0.760594 | 72.222% |
| 2 | 0 | 165052.4 | 23.176% | 1.847968 | 74.521% | 0.033920 | 0.557268 | 0.200566 | 0.732811 | 68.116% |
| 3 | 0 | 174500.5 | 30.227% | 1.767554 | 75.630% | 0.032528 | 0.516351 | 0.194856 | 0.718822 | 66.163% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

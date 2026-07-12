# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147463.4 | 0.000% | 8.001819 | 0.000% | 0.245632 | 2.407822 | 0.186586 | 0.878468 | 89.031% |
| 0.25 | 0 | 156567.9 | 6.174% | 6.762027 | 15.494% | 0.202652 | 2.316829 | 0.265452 | 0.872149 | 87.730% |
| 0.5 | 0 | 165021.3 | 11.907% | 4.748725 | 40.654% | 0.125820 | 2.009247 | 0.350903 | 0.847114 | 83.482% |
| 1 | 0 | 175980.8 | 19.339% | 3.525533 | 55.941% | 0.077422 | 1.661198 | 0.360570 | 0.821708 | 79.046% |
| 2 | 0 | 193979.4 | 31.544% | 3.009946 | 62.384% | 0.067913 | 1.416714 | 0.356596 | 0.806385 | 75.827% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

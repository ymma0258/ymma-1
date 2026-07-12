# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 6.466806 | 0.000% | 0.192116 | 2.132585 | 0.231219 | 0.867789 | 86.826% |
| 0.25 | 0 | 154295.5 | 4.965% | 5.209805 | 19.438% | 0.155423 | 1.928984 | 0.271285 | 0.857832 | 84.382% |
| 0.5 | 0 | 160886.5 | 9.449% | 3.571571 | 44.771% | 0.077716 | 1.280521 | 0.257443 | 0.813502 | 77.750% |
| 1 | 0 | 167841.1 | 14.180% | 2.195748 | 66.046% | 0.042113 | 0.678595 | 0.185132 | 0.723994 | 64.886% |
| 2 | 0 | 177884.9 | 21.012% | 1.631347 | 74.774% | 0.028022 | 0.509879 | 0.177340 | 0.658219 | 54.953% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

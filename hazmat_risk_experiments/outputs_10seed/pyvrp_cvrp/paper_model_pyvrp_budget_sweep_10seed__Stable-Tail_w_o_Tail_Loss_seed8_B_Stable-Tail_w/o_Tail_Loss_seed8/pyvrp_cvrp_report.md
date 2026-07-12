# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.0 | 0.000% | 6.679284 | 0.000% | 0.178162 | 2.066060 | 0.193395 | 0.866559 | 89.346% |
| 0.25 | 0 | 157201.1 | 6.748% | 5.462098 | 18.223% | 0.138815 | 1.646584 | 0.206288 | 0.865566 | 88.544% |
| 0.5 | 0 | 166220.5 | 12.872% | 4.527155 | 32.221% | 0.124589 | 1.323788 | 0.184745 | 0.861753 | 87.038% |
| 1 | 0 | 176841.7 | 20.085% | 2.769023 | 58.543% | 0.063607 | 0.944543 | 0.276823 | 0.811888 | 79.089% |
| 2 | 0 | 191807.7 | 30.248% | 2.204215 | 66.999% | 0.046145 | 0.702654 | 0.247692 | 0.783814 | 73.819% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

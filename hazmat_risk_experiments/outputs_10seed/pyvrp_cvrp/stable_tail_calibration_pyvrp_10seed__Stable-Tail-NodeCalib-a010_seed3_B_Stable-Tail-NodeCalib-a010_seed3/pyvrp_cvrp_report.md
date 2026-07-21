# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 6.943119 | 0.000% | 0.189865 | 2.324081 | 0.242881 | 0.868867 | 88.875% |
| 0.25 | 0 | 155253.2 | 5.664% | 5.787080 | 16.650% | 0.142685 | 2.113062 | 0.272060 | 0.862966 | 87.831% |
| 0.5 | 0 | 163253.6 | 11.109% | 4.656883 | 32.928% | 0.119589 | 1.532603 | 0.236920 | 0.852543 | 85.542% |
| 1 | 0 | 174536.1 | 18.788% | 3.508533 | 49.467% | 0.095096 | 1.349238 | 0.292058 | 0.837950 | 82.154% |
| 2 | 0 | 192401.2 | 30.947% | 2.759423 | 60.257% | 0.068645 | 1.140641 | 0.303808 | 0.809002 | 77.606% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 6.886569 | 0.000% | 0.217812 | 2.395161 | 0.255898 | 0.873925 | 89.972% |
| 0.25 | 0 | 155776.5 | 5.972% | 5.359972 | 22.168% | 0.149327 | 1.806278 | 0.262779 | 0.868110 | 88.245% |
| 0.5 | 0 | 163938.2 | 11.525% | 4.667063 | 32.229% | 0.126002 | 1.392541 | 0.205148 | 0.859770 | 86.744% |
| 1 | 0 | 173640.1 | 18.125% | 2.771110 | 59.761% | 0.062079 | 0.968078 | 0.263411 | 0.814592 | 79.165% |
| 2 | 0 | 187140.2 | 27.309% | 2.255886 | 67.242% | 0.044683 | 0.786564 | 0.259038 | 0.793772 | 75.504% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.938070 | 0.000% | 0.305060 | 3.409897 | 0.250389 | 0.878131 | 90.980% |
| 0.5 | 0 | 166122.4 | 13.216% | 7.135140 | 28.204% | 0.192876 | 2.396540 | 0.255120 | 0.875369 | 88.745% |
| 1 | 0 | 178303.2 | 21.517% | 4.560062 | 54.115% | 0.122870 | 1.689929 | 0.313991 | 0.852063 | 83.766% |
| 1.5 | 0 | 188059.5 | 28.166% | 3.932576 | 60.429% | 0.100201 | 1.531940 | 0.289856 | 0.840890 | 81.366% |
| 2 | 0 | 196747.3 | 34.087% | 3.635389 | 63.420% | 0.090005 | 1.568240 | 0.359074 | 0.830375 | 79.629% |
| 3 | 0 | 213211.1 | 45.308% | 3.542045 | 64.359% | 0.084426 | 1.551119 | 0.393369 | 0.826516 | 78.902% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

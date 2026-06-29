# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.938070 | 0.000% | 0.305060 | 3.409897 | 0.250389 | 0.878131 | 90.980% |
| 1 | 0 | 178303.2 | 21.517% | 4.560062 | 54.115% | 0.122870 | 1.689929 | 0.313991 | 0.852063 | 83.766% |
| 1 | 0.5 | 186567.6 | 27.149% | 3.889402 | 60.864% | 0.098108 | 1.538466 | 0.303046 | 0.839195 | 81.205% |
| 1 | 1 | 193699.0 | 32.010% | 3.677758 | 62.993% | 0.091856 | 1.523729 | 0.344801 | 0.832706 | 80.031% |
| 1 | 2 | 206931.5 | 41.028% | 3.541601 | 64.363% | 0.087280 | 1.563621 | 0.343341 | 0.826112 | 79.001% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147063.6 | 0.000% | 6.799193 | 0.000% | 0.191962 | 2.190531 | 0.236550 | 0.877954 | 89.470% |
| 0.25 | 0 | 156655.4 | 6.522% | 5.555709 | 18.289% | 0.136826 | 2.024107 | 0.274271 | 0.869663 | 88.010% |
| 0.5 | 0 | 164777.1 | 12.045% | 4.124881 | 39.333% | 0.106013 | 1.261661 | 0.188886 | 0.853029 | 84.714% |
| 1 | 0 | 175364.6 | 19.244% | 2.708189 | 60.169% | 0.066376 | 1.022891 | 0.294586 | 0.808881 | 77.768% |
| 2 | 0 | 190665.6 | 29.648% | 2.137395 | 68.564% | 0.044517 | 0.818060 | 0.301194 | 0.772227 | 71.616% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

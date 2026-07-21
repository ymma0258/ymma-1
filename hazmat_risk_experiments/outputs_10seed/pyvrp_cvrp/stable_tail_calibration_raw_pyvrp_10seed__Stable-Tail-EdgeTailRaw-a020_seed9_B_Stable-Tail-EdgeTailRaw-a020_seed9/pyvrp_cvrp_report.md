# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.2 | 0.000% | 9.229313 | 0.000% | 0.289887 | 3.115157 | 0.233781 | 0.873220 | 90.337% |
| 0.25 | 0 | 158984.4 | 7.861% | 7.835512 | 15.102% | 0.227503 | 2.749144 | 0.263091 | 0.869354 | 89.456% |
| 0.5 | 0 | 168239.2 | 14.140% | 5.528893 | 40.094% | 0.146918 | 1.656703 | 0.220603 | 0.854231 | 86.270% |
| 1 | 0 | 179176.8 | 21.561% | 3.491961 | 62.164% | 0.078418 | 1.214397 | 0.297406 | 0.811218 | 79.180% |
| 2 | 0 | 197052.4 | 33.688% | 3.168007 | 65.675% | 0.063610 | 0.992209 | 0.240951 | 0.797872 | 76.912% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

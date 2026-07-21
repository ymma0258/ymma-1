# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.1 | 0.000% | 9.103035 | 0.000% | 0.279653 | 3.407836 | 0.310878 | 0.876449 | 89.745% |
| 0.25 | 0 | 156752.9 | 6.588% | 7.926502 | 12.925% | 0.238214 | 3.078084 | 0.309687 | 0.875238 | 89.436% |
| 0.5 | 0 | 165376.2 | 12.452% | 5.902223 | 35.162% | 0.167543 | 2.144932 | 0.248305 | 0.859290 | 86.449% |
| 1 | 0 | 177645.6 | 20.795% | 4.262674 | 53.173% | 0.107936 | 1.738182 | 0.331368 | 0.840422 | 82.541% |
| 2 | 0 | 195992.0 | 33.270% | 3.675616 | 59.622% | 0.090852 | 1.588145 | 0.340549 | 0.826190 | 80.076% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

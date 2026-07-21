# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 6.195791 | 0.000% | 0.182802 | 1.826030 | 0.166809 | 0.871357 | 88.787% |
| 0.25 | 0 | 141918.2 | 5.911% | 4.131986 | 33.310% | 0.117727 | 1.296245 | 0.189053 | 0.853015 | 86.142% |
| 0.5 | 0 | 147083.2 | 9.765% | 3.214386 | 48.120% | 0.092384 | 1.023483 | 0.229257 | 0.834806 | 83.077% |
| 1 | 0 | 155183.2 | 15.810% | 2.098578 | 66.129% | 0.053582 | 0.651858 | 0.233406 | 0.768159 | 74.158% |
| 2 | 0 | 167653.2 | 25.116% | 1.958162 | 68.395% | 0.048839 | 0.644729 | 0.244479 | 0.753295 | 71.709% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

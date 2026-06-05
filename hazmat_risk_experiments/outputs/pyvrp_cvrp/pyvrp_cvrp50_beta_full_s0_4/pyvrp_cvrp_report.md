# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 143250.0 | 0.000% | 8.629877 | 0.000% | 0.192865 | 2.442272 | 0.185174 | 0.921784 | 98.285% |
| 0.25 | 150813.4 | 5.280% | 4.964453 | 42.474% | 0.017288 | 1.715981 | 0.332657 | 0.945058 | 100.000% |
| 0.5 | 155058.2 | 8.243% | 3.062040 | 64.518% | 0.010483 | 1.174659 | 0.356135 | 0.967838 | 100.000% |
| 1 | 160792.2 | 12.246% | 1.998426 | 76.843% | 0.006709 | 0.666126 | 0.266821 | 0.981098 | 100.000% |
| 2 | 169081.2 | 18.032% | 1.687239 | 80.449% | 0.005600 | 0.768605 | 0.463934 | 0.984791 | 100.000% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

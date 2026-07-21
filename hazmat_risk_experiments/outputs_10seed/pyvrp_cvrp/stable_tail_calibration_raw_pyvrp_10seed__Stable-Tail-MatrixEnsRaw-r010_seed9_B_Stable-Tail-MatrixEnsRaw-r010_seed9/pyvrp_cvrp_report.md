# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.2 | 0.000% | 8.074844 | 0.000% | 0.249244 | 2.573807 | 0.218629 | 0.870739 | 90.008% |
| 0.25 | 0 | 158090.8 | 7.498% | 6.937387 | 14.086% | 0.190729 | 2.234240 | 0.204873 | 0.869934 | 89.497% |
| 0.5 | 0 | 167962.7 | 14.210% | 4.629217 | 42.671% | 0.123319 | 1.585126 | 0.274764 | 0.844074 | 84.948% |
| 1 | 0 | 179208.9 | 21.858% | 3.088726 | 61.749% | 0.064382 | 1.008547 | 0.254310 | 0.808516 | 78.676% |
| 2 | 0 | 195956.9 | 33.246% | 2.681250 | 66.795% | 0.053299 | 0.850037 | 0.241470 | 0.790007 | 75.977% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 9.260107 | 0.000% | 0.293948 | 2.763098 | 0.179551 | 0.874121 | 89.915% |
| 0.25 | 0 | 143562.8 | 6.872% | 5.964074 | 35.594% | 0.171404 | 1.941177 | 0.233615 | 0.859662 | 87.681% |
| 0.5 | 0 | 149674.4 | 11.422% | 4.694714 | 49.302% | 0.120466 | 1.875618 | 0.277907 | 0.836502 | 84.650% |
| 1 | 0 | 159019.4 | 18.378% | 3.142284 | 66.066% | 0.078912 | 1.109963 | 0.271560 | 0.789449 | 77.673% |
| 2 | 0 | 172588.8 | 28.480% | 2.543248 | 72.535% | 0.057802 | 0.768530 | 0.219924 | 0.756330 | 72.759% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

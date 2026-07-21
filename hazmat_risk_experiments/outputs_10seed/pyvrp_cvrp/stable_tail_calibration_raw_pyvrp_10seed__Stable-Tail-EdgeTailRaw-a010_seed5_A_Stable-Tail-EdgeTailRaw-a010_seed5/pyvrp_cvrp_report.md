# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.4 | 0.000% | 7.219021 | 0.000% | 0.229125 | 2.091882 | 0.162453 | 0.871945 | 88.681% |
| 0.25 | 0 | 142409.9 | 6.172% | 5.320771 | 26.295% | 0.148025 | 1.648004 | 0.217915 | 0.859558 | 86.516% |
| 0.5 | 0 | 147624.9 | 10.060% | 3.593008 | 50.229% | 0.103329 | 1.601178 | 0.375396 | 0.825956 | 81.484% |
| 1 | 0 | 155661.3 | 16.051% | 2.547591 | 64.710% | 0.066559 | 1.002764 | 0.296242 | 0.775055 | 74.247% |
| 2 | 0 | 166704.3 | 24.284% | 1.935672 | 73.186% | 0.042743 | 0.625720 | 0.229548 | 0.724667 | 66.635% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

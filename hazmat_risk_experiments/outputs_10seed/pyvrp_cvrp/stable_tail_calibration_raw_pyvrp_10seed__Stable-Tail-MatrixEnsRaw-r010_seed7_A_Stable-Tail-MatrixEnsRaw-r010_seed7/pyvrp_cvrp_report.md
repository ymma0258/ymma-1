# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.8 | 0.000% | 7.729336 | 0.000% | 0.245483 | 2.198450 | 0.173446 | 0.871960 | 89.223% |
| 0.25 | 0 | 142955.8 | 6.632% | 5.397266 | 30.172% | 0.162449 | 1.660588 | 0.198716 | 0.860603 | 86.864% |
| 0.5 | 0 | 149258.9 | 11.333% | 4.090390 | 47.080% | 0.120042 | 1.340658 | 0.225734 | 0.837761 | 83.278% |
| 1 | 0 | 158667.2 | 18.351% | 2.892401 | 62.579% | 0.078211 | 1.206809 | 0.321385 | 0.795803 | 76.824% |
| 2 | 0 | 171808.3 | 28.153% | 2.333157 | 69.814% | 0.054346 | 0.711702 | 0.213331 | 0.759473 | 71.258% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

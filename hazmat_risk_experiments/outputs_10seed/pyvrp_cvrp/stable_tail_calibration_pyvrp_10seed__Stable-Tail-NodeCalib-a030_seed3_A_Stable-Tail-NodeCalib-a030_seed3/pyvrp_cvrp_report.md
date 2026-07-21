# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 6.640120 | 0.000% | 0.197593 | 1.962689 | 0.168529 | 0.868551 | 88.332% |
| 0.25 | 0 | 141564.4 | 5.647% | 4.927381 | 25.794% | 0.145061 | 1.571460 | 0.227731 | 0.859802 | 87.133% |
| 0.5 | 0 | 146979.1 | 9.687% | 3.611574 | 45.610% | 0.106885 | 1.351560 | 0.268170 | 0.830786 | 82.923% |
| 1 | 0 | 154771.5 | 15.503% | 2.350487 | 64.602% | 0.060845 | 0.714761 | 0.222165 | 0.766142 | 73.735% |
| 2 | 0 | 166377.7 | 24.164% | 2.106479 | 68.276% | 0.052107 | 0.680558 | 0.265147 | 0.748597 | 70.993% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.7 | 0.000% | 5.423402 | 0.000% | 0.149542 | 1.763836 | 0.239770 | 0.880200 | 89.860% |
| 0.25 | 0 | 156537.5 | 6.297% | 4.747836 | 12.456% | 0.118166 | 1.582605 | 0.245998 | 0.877654 | 89.093% |
| 0.5 | 0 | 165021.3 | 12.058% | 3.224253 | 40.549% | 0.082706 | 1.050878 | 0.225173 | 0.851336 | 84.528% |
| 1 | 0 | 175051.3 | 18.869% | 2.172153 | 59.949% | 0.054099 | 0.806287 | 0.289901 | 0.812389 | 78.314% |
| 2 | 0 | 190299.1 | 29.223% | 1.751222 | 67.710% | 0.037562 | 0.626406 | 0.260282 | 0.785627 | 73.578% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

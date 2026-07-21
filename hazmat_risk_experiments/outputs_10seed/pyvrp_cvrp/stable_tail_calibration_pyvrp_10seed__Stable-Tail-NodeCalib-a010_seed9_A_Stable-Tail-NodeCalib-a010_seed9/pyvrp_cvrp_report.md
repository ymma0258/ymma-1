# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 8.278089 | 0.000% | 0.263971 | 2.377454 | 0.168055 | 0.869546 | 89.311% |
| 0.25 | 0 | 143140.2 | 6.769% | 5.841314 | 29.436% | 0.170281 | 1.808435 | 0.213381 | 0.858210 | 87.513% |
| 0.5 | 0 | 149416.3 | 11.451% | 4.332778 | 47.660% | 0.106186 | 1.631653 | 0.233173 | 0.828661 | 83.606% |
| 1 | 0 | 158622.5 | 18.318% | 2.839536 | 65.698% | 0.064093 | 0.981617 | 0.268131 | 0.770076 | 75.247% |
| 2 | 0 | 172519.8 | 28.684% | 2.435484 | 70.579% | 0.052639 | 0.729117 | 0.201087 | 0.747170 | 71.764% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

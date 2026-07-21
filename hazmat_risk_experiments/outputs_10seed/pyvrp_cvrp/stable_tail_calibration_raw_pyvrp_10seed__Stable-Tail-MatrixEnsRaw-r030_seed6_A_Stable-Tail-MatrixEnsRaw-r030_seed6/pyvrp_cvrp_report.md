# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.3 | 0.000% | 5.694210 | 0.000% | 0.166394 | 1.628860 | 0.160455 | 0.868297 | 88.946% |
| 0.25 | 0 | 143253.6 | 6.907% | 3.581552 | 37.102% | 0.102405 | 1.237733 | 0.268369 | 0.847744 | 85.492% |
| 0.5 | 0 | 149317.8 | 11.433% | 2.911491 | 48.869% | 0.086277 | 1.104673 | 0.313299 | 0.823147 | 82.428% |
| 1 | 0 | 158832.2 | 18.533% | 2.062113 | 63.786% | 0.055621 | 0.640510 | 0.248898 | 0.780973 | 76.242% |
| 2 | 0 | 173058.2 | 29.150% | 1.649055 | 71.040% | 0.038555 | 0.601901 | 0.291996 | 0.738384 | 70.305% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

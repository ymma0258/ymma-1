# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 8.087424 | 0.000% | 0.256422 | 2.440156 | 0.192799 | 0.879980 | 89.811% |
| 0.25 | 0 | 142780.9 | 6.290% | 5.319569 | 34.224% | 0.153917 | 1.646194 | 0.229554 | 0.863960 | 86.871% |
| 0.5 | 0 | 148654.3 | 10.662% | 3.854747 | 52.337% | 0.112722 | 1.421449 | 0.293708 | 0.834810 | 82.521% |
| 1 | 0 | 156276.9 | 16.337% | 2.637809 | 67.384% | 0.070311 | 1.033109 | 0.287257 | 0.783300 | 75.063% |
| 2 | 0 | 167148.5 | 24.430% | 1.911632 | 76.363% | 0.042065 | 0.631796 | 0.244373 | 0.721591 | 66.069% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

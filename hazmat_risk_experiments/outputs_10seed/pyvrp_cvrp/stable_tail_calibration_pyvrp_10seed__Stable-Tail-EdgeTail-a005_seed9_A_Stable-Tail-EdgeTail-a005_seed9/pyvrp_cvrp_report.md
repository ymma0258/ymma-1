# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 8.544774 | 0.000% | 0.275786 | 2.695058 | 0.189385 | 0.871576 | 89.489% |
| 0.25 | 0 | 143128.8 | 6.655% | 5.560156 | 34.929% | 0.155878 | 1.762880 | 0.217628 | 0.853921 | 86.858% |
| 0.5 | 0 | 149505.9 | 11.407% | 4.254330 | 50.211% | 0.108718 | 1.621179 | 0.278900 | 0.821764 | 82.861% |
| 1 | 0 | 158578.5 | 18.167% | 2.995077 | 64.948% | 0.068115 | 1.006431 | 0.231629 | 0.778985 | 76.578% |
| 2 | 0 | 172470.1 | 28.519% | 2.414261 | 71.746% | 0.052354 | 0.695628 | 0.193639 | 0.741422 | 70.945% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

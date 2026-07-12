# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.9 | 0.000% | 7.359192 | 0.000% | 0.215799 | 2.205865 | 0.167225 | 0.857187 | 88.325% |
| 0.25 | 0 | 142694.1 | 6.437% | 5.522601 | 24.956% | 0.158542 | 1.651801 | 0.181896 | 0.845754 | 86.762% |
| 0.5 | 0 | 148979.1 | 11.125% | 4.142324 | 43.712% | 0.120226 | 1.385195 | 0.234583 | 0.821689 | 83.202% |
| 1 | 0 | 158270.1 | 18.055% | 2.865241 | 61.066% | 0.075913 | 0.921446 | 0.214887 | 0.766842 | 75.935% |
| 2 | 0 | 171803.5 | 28.150% | 2.413547 | 67.204% | 0.057964 | 0.824196 | 0.278314 | 0.729485 | 70.691% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

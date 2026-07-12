# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.5 | 0.000% | 9.527244 | 0.000% | 0.308039 | 2.798518 | 0.157631 | 0.854629 | 88.084% |
| 0.25 | 0 | 145307.7 | 8.171% | 6.954583 | 27.003% | 0.180773 | 2.072858 | 0.186709 | 0.848413 | 86.841% |
| 0.5 | 0 | 152598.4 | 13.598% | 5.027873 | 47.226% | 0.139216 | 1.655446 | 0.235887 | 0.815347 | 82.198% |
| 1 | 0 | 163487.2 | 21.704% | 3.627194 | 61.928% | 0.081951 | 1.270143 | 0.272026 | 0.769461 | 75.636% |
| 2 | 0 | 178876.7 | 33.161% | 2.697582 | 71.686% | 0.046367 | 0.934735 | 0.275271 | 0.707537 | 67.845% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

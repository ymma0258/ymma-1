# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.701649 | 0.000% | 0.270892 | 2.469651 | 0.147285 | 0.874652 | 89.737% |
| 0.25 | 0 | 143091.2 | 6.786% | 6.029559 | 30.708% | 0.179293 | 1.830560 | 0.209353 | 0.865537 | 87.352% |
| 0.5 | 0 | 149196.9 | 11.343% | 4.567524 | 47.510% | 0.116005 | 1.451106 | 0.184931 | 0.845575 | 84.079% |
| 1 | 0 | 158498.5 | 18.285% | 3.260477 | 62.530% | 0.072756 | 1.191802 | 0.291764 | 0.805873 | 77.756% |
| 2 | 0 | 170864.4 | 27.513% | 2.535759 | 70.859% | 0.048612 | 0.808732 | 0.260480 | 0.765709 | 71.399% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

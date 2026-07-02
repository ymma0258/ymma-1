# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.206917 | 0.000% | 0.247066 | 2.675116 | 0.222401 | 0.842545 | 86.792% |
| 0.5 | 0 | 166120.2 | 13.214% | 4.167703 | 49.217% | 0.092341 | 1.390130 | 0.252678 | 0.755362 | 75.757% |
| 1 | 0 | 176630.7 | 20.377% | 3.404748 | 58.514% | 0.073281 | 0.997633 | 0.218171 | 0.707254 | 70.076% |
| 1.5 | 0 | 185474.7 | 26.405% | 3.042144 | 62.932% | 0.063197 | 0.988041 | 0.254895 | 0.681926 | 66.641% |
| 2 | 0 | 193392.4 | 31.801% | 2.803399 | 65.841% | 0.053338 | 1.060942 | 0.265194 | 0.661305 | 63.915% |
| 3 | 0 | 207936.4 | 41.713% | 2.704324 | 67.048% | 0.050138 | 1.089226 | 0.271677 | 0.656776 | 63.087% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

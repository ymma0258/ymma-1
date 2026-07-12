# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134597.6 | 0.000% | 8.953105 | 0.000% | 0.294644 | 2.539016 | 0.158893 | 0.859371 | 88.388% |
| 0.25 | 0 | 143678.6 | 6.747% | 6.386201 | 28.671% | 0.170958 | 1.905624 | 0.188898 | 0.850684 | 87.228% |
| 0.5 | 0 | 150452.1 | 11.779% | 4.943719 | 44.782% | 0.128620 | 1.509572 | 0.198200 | 0.828775 | 84.002% |
| 1 | 0 | 159927.2 | 18.819% | 3.290878 | 63.243% | 0.084292 | 1.158524 | 0.274420 | 0.776134 | 76.489% |
| 2 | 0 | 176055.7 | 30.802% | 2.813139 | 68.579% | 0.068453 | 0.933297 | 0.268779 | 0.748738 | 72.425% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

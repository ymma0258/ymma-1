# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 4.607974 | 0.000% | 0.142052 | 1.489269 | 0.204363 | 0.863144 | 88.142% |
| 0.25 | 0 | 156092.1 | 6.380% | 3.740481 | 18.826% | 0.086403 | 1.285742 | 0.229447 | 0.854486 | 86.749% |
| 0.5 | 0 | 164321.6 | 11.988% | 2.842255 | 38.319% | 0.070280 | 0.937124 | 0.219639 | 0.838019 | 83.481% |
| 1 | 0 | 175054.1 | 19.303% | 1.884624 | 59.101% | 0.045124 | 0.593479 | 0.197329 | 0.785763 | 76.119% |
| 2 | 0 | 188980.1 | 28.794% | 1.480186 | 67.878% | 0.032603 | 0.414599 | 0.176239 | 0.752406 | 70.773% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

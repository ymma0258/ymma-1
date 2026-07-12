# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 8.040894 | 0.000% | 0.205225 | 2.299408 | 0.172334 | 0.867538 | 88.997% |
| 0.25 | 0 | 157979.9 | 7.471% | 6.867596 | 14.592% | 0.187345 | 2.089406 | 0.218306 | 0.865848 | 87.959% |
| 0.5 | 0 | 167373.7 | 13.862% | 3.914254 | 51.321% | 0.095218 | 1.219228 | 0.222094 | 0.813907 | 79.194% |
| 1 | 0 | 177590.7 | 20.812% | 3.164077 | 60.650% | 0.070722 | 1.054943 | 0.214381 | 0.785732 | 74.695% |
| 2 | 0 | 195505.7 | 33.000% | 2.457564 | 69.437% | 0.048887 | 0.991512 | 0.308538 | 0.743687 | 67.706% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

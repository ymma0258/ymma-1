# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 8.001621 | 0.000% | 0.242379 | 2.435645 | 0.187419 | 0.878218 | 90.555% |
| 0.25 | 0 | 157614.4 | 7.271% | 6.364782 | 20.456% | 0.187814 | 1.862205 | 0.191482 | 0.876949 | 89.354% |
| 0.5 | 0 | 166895.4 | 13.588% | 4.952750 | 38.103% | 0.135432 | 1.735958 | 0.260321 | 0.858622 | 86.160% |
| 1 | 0 | 178362.2 | 21.392% | 3.285145 | 58.944% | 0.080466 | 1.136663 | 0.269346 | 0.832154 | 81.084% |
| 2 | 0 | 195209.3 | 32.858% | 2.721034 | 65.994% | 0.061525 | 0.847429 | 0.208904 | 0.810360 | 77.432% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

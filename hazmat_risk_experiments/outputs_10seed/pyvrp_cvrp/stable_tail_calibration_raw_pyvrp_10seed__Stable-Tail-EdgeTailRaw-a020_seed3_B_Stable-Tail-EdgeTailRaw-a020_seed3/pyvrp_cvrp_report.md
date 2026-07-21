# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.2 | 0.000% | 7.045343 | 0.000% | 0.208231 | 2.380872 | 0.242620 | 0.869346 | 88.991% |
| 0.25 | 0 | 155355.3 | 5.542% | 5.816545 | 17.441% | 0.145294 | 2.137478 | 0.269149 | 0.866558 | 88.080% |
| 0.5 | 0 | 163329.7 | 10.960% | 4.762383 | 32.404% | 0.120081 | 1.859189 | 0.280701 | 0.855596 | 85.882% |
| 1 | 0 | 175431.1 | 19.181% | 3.452997 | 50.989% | 0.087338 | 1.469757 | 0.316152 | 0.833975 | 81.798% |
| 2 | 0 | 192798.1 | 30.979% | 2.833342 | 59.784% | 0.069626 | 1.199663 | 0.314037 | 0.813249 | 78.196% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

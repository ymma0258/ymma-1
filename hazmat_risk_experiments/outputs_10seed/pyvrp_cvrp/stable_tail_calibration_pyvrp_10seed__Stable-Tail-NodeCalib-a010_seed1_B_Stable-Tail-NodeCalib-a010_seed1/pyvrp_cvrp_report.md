# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 9.761168 | 0.000% | 0.311230 | 3.392386 | 0.254199 | 0.873101 | 89.857% |
| 0.25 | 0 | 155946.7 | 6.088% | 7.918422 | 18.878% | 0.238589 | 2.376221 | 0.204772 | 0.869889 | 88.655% |
| 0.5 | 0 | 164077.4 | 11.619% | 6.812567 | 30.207% | 0.197839 | 1.961505 | 0.181800 | 0.861361 | 87.138% |
| 1 | 0 | 173781.7 | 18.221% | 4.030816 | 58.706% | 0.095859 | 1.408816 | 0.250554 | 0.816513 | 79.577% |
| 2 | 0 | 187622.4 | 27.637% | 3.225055 | 66.960% | 0.062770 | 1.176344 | 0.295543 | 0.792322 | 75.233% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 7.960388 | 0.000% | 0.243144 | 2.567704 | 0.217693 | 0.876687 | 89.389% |
| 0.25 | 0 | 156703.6 | 6.410% | 6.648672 | 16.478% | 0.173024 | 2.271648 | 0.239998 | 0.869747 | 88.194% |
| 0.5 | 0 | 165100.7 | 12.112% | 4.895888 | 38.497% | 0.113474 | 1.597532 | 0.261002 | 0.843007 | 84.117% |
| 1 | 0 | 175584.8 | 19.231% | 3.274955 | 58.859% | 0.079660 | 1.189623 | 0.296483 | 0.810267 | 78.155% |
| 2 | 0 | 191748.1 | 30.207% | 2.845835 | 64.250% | 0.068422 | 0.942730 | 0.288018 | 0.795906 | 75.714% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

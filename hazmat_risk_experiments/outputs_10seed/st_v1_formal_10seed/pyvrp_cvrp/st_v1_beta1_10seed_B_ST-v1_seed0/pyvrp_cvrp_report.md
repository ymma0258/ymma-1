# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.003160 | 0.000% | 0.253942 | 2.625387 | 0.223399 | 0.881536 | 90.545% |
| 1 | 0 | 176640.6 | 20.384% | 2.951393 | 63.122% | 0.062418 | 1.065370 | 0.288607 | 0.818926 | 78.903% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

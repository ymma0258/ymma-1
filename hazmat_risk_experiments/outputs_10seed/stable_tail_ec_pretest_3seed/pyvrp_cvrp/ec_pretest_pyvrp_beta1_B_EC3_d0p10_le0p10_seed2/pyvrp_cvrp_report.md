# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.836275 | 0.000% | 0.295165 | 3.040816 | 0.189822 | 0.871097 | 90.699% |
| 1 | 0 | 180753.2 | 23.187% | 4.404909 | 55.218% | 0.120965 | 1.551060 | 0.287358 | 0.845971 | 83.815% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

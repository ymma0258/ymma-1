# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.206917 | 0.000% | 0.247066 | 2.675116 | 0.222401 | 0.842545 | 86.792% |
| 1 | 0 | 176653.2 | 20.393% | 3.429416 | 58.213% | 0.074104 | 0.998302 | 0.211661 | 0.709609 | 70.357% |
| 1 | 1 | 189535.4 | 29.172% | 2.828733 | 65.532% | 0.055989 | 1.045751 | 0.257197 | 0.666120 | 64.411% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

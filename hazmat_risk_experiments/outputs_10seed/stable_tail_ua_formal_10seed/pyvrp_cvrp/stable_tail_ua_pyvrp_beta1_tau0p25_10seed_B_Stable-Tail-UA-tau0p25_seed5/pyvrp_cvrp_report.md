# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 11.844017 | 0.000% | 0.299806 | 3.717459 | 0.196006 | 0.850723 | 88.263% |
| 1 | 0 | 183867.5 | 25.309% | 5.726477 | 51.651% | 0.115364 | 2.121586 | 0.330717 | 0.799453 | 80.741% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.3 | 0.000% | 8.700364 | 0.000% | 0.273654 | 3.233327 | 0.310847 | 0.873306 | 89.553% |
| 0.25 | 0 | 157124.9 | 6.696% | 7.432479 | 14.573% | 0.224125 | 2.678606 | 0.279413 | 0.872867 | 88.947% |
| 0.5 | 0 | 165522.8 | 12.398% | 6.367293 | 26.816% | 0.178255 | 2.272495 | 0.278310 | 0.859945 | 87.004% |
| 1 | 0 | 178420.1 | 21.156% | 4.347118 | 50.035% | 0.114438 | 1.686735 | 0.287675 | 0.840100 | 82.749% |
| 2 | 0 | 197426.8 | 34.063% | 3.553442 | 59.158% | 0.087664 | 1.591584 | 0.361585 | 0.822673 | 79.464% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

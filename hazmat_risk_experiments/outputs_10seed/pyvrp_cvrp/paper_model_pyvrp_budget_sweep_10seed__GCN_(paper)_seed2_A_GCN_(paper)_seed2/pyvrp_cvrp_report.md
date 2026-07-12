# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.9 | 0.000% | 8.831531 | 0.000% | 0.283324 | 2.563646 | 0.165717 | 0.865726 | 89.244% |
| 0.25 | 0 | 142867.9 | 6.566% | 6.501241 | 26.386% | 0.189646 | 2.046190 | 0.223091 | 0.856318 | 87.849% |
| 0.5 | 0 | 149437.3 | 11.466% | 5.150846 | 41.677% | 0.153759 | 1.725830 | 0.223722 | 0.843144 | 85.458% |
| 1 | 0 | 159816.9 | 19.209% | 3.658612 | 58.573% | 0.096774 | 1.397382 | 0.322336 | 0.804419 | 79.705% |
| 2 | 0 | 175363.0 | 30.805% | 3.268215 | 62.994% | 0.079905 | 1.128398 | 0.297383 | 0.787430 | 77.072% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

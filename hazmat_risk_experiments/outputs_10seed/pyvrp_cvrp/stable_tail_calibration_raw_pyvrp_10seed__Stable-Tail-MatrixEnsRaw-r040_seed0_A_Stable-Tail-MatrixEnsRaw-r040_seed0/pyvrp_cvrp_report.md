# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 5.063906 | 0.000% | 0.159676 | 1.573221 | 0.209759 | 0.888774 | 90.928% |
| 0.25 | 0 | 142234.8 | 5.936% | 2.871491 | 43.295% | 0.087417 | 1.012208 | 0.254769 | 0.865415 | 86.843% |
| 0.5 | 0 | 147787.7 | 10.072% | 2.341982 | 53.751% | 0.070077 | 0.987743 | 0.317962 | 0.844277 | 83.940% |
| 1 | 0 | 155379.3 | 15.726% | 1.473075 | 70.910% | 0.035569 | 0.613822 | 0.321438 | 0.786894 | 75.213% |
| 2 | 0 | 166652.0 | 24.122% | 1.135998 | 77.567% | 0.020412 | 0.372349 | 0.235322 | 0.738801 | 68.210% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

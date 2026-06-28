# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 9.407569 | 0.000% | 0.268733 | 2.766042 | 0.146956 | 0.858310 | 89.319% |
| 1 | 0 | 160932.1 | 20.101% | 3.903812 | 58.504% | 0.106260 | 1.338075 | 0.243396 | 0.787095 | 78.433% |
| 1 | 1 | 172812.3 | 28.967% | 2.807066 | 70.162% | 0.055220 | 0.935882 | 0.283414 | 0.726050 | 69.897% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

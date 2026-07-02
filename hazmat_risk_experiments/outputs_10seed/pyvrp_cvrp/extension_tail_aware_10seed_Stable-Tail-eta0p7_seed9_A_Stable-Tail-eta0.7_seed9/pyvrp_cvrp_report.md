# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 9.621908 | 0.000% | 0.204897 | 2.949665 | 0.192345 | 0.873943 | 89.228% |
| 1 | 0 | 154039.6 | 14.957% | 2.860886 | 70.267% | 0.042643 | 1.170588 | 0.308646 | 0.744864 | 69.923% |
| 2 | 0 | 164386.4 | 22.679% | 2.399035 | 75.067% | 0.034276 | 0.769379 | 0.227090 | 0.714819 | 65.690% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 8.776531 | 0.000% | 0.289341 | 2.640513 | 0.177326 | 0.870735 | 88.849% |
| 0.25 | 0 | 143764.3 | 7.128% | 5.958786 | 32.105% | 0.153337 | 1.840724 | 0.199731 | 0.854873 | 86.117% |
| 0.5 | 0 | 150242.1 | 11.955% | 4.622847 | 47.327% | 0.117470 | 1.762420 | 0.274022 | 0.829096 | 82.434% |
| 1 | 0 | 159460.6 | 18.825% | 3.086063 | 64.837% | 0.081407 | 1.394705 | 0.375459 | 0.783061 | 74.793% |
| 2 | 0 | 172490.3 | 28.534% | 2.538283 | 71.079% | 0.059073 | 0.787734 | 0.219442 | 0.751427 | 69.961% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

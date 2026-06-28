# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 12.702124 | 0.000% | 0.320277 | 3.998947 | 0.198789 | 0.857420 | 89.026% |
| 1.5 | 1 | 216893.1 | 47.817% | 4.656708 | 63.339% | 0.088038 | 1.983532 | 0.373395 | 0.767751 | 75.237% |
| 2 | 1 | 227729.7 | 55.202% | 4.663866 | 63.283% | 0.088447 | 1.752012 | 0.332725 | 0.767123 | 75.233% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

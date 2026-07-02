# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.519431 | 0.000% | 0.251641 | 2.779042 | 0.217431 | 0.841806 | 87.151% |
| 0.5 | 0 | 165135.3 | 12.543% | 6.095173 | 28.456% | 0.158419 | 1.988897 | 0.263793 | 0.814441 | 83.009% |
| 1 | 0 | 177391.9 | 20.896% | 4.191568 | 50.800% | 0.101618 | 1.679518 | 0.337492 | 0.758458 | 75.839% |
| 1.5 | 0 | 187499.2 | 27.784% | 3.703254 | 56.532% | 0.069073 | 1.388253 | 0.288971 | 0.731099 | 72.250% |
| 2 | 0 | 195799.6 | 33.441% | 3.399072 | 60.102% | 0.061915 | 1.336940 | 0.315184 | 0.710265 | 69.565% |
| 3 | 0 | 211224.3 | 43.954% | 3.190288 | 62.553% | 0.056675 | 1.328446 | 0.333914 | 0.697111 | 67.859% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 9.190819 | 0.000% | 0.197477 | 2.832182 | 0.181701 | 0.880898 | 89.597% |
| 1 | 0 | 154721.7 | 15.466% | 3.010552 | 67.244% | 0.049965 | 1.070853 | 0.254487 | 0.786931 | 74.243% |
| 2 | 0 | 165126.6 | 23.231% | 2.306770 | 74.901% | 0.034333 | 0.694718 | 0.226212 | 0.743135 | 67.552% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

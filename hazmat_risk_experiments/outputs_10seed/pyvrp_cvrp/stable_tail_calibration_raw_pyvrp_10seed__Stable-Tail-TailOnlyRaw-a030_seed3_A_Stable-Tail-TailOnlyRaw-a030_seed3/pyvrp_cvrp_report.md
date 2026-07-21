# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.9 | 0.000% | 7.788341 | 0.000% | 0.249880 | 2.485630 | 0.199643 | 0.876209 | 89.318% |
| 0.25 | 0 | 141994.1 | 5.652% | 5.251271 | 32.575% | 0.152344 | 1.506282 | 0.156916 | 0.863790 | 87.708% |
| 0.5 | 0 | 147698.0 | 9.896% | 3.899042 | 49.937% | 0.116105 | 1.433383 | 0.271164 | 0.841782 | 84.179% |
| 1 | 0 | 155257.6 | 15.521% | 2.465125 | 68.349% | 0.063795 | 0.791829 | 0.246797 | 0.775334 | 74.848% |
| 2 | 0 | 167628.6 | 24.726% | 2.256859 | 71.023% | 0.056130 | 0.740892 | 0.246480 | 0.765154 | 72.945% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

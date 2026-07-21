# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 9.019449 | 0.000% | 0.280259 | 3.437936 | 0.309144 | 0.875302 | 89.608% |
| 0.25 | 0 | 156834.2 | 6.692% | 7.615824 | 15.562% | 0.230968 | 3.101600 | 0.326197 | 0.871162 | 88.802% |
| 0.5 | 0 | 165343.7 | 12.481% | 6.349173 | 29.606% | 0.172896 | 2.447092 | 0.285619 | 0.864646 | 87.205% |
| 1 | 0 | 177473.0 | 20.732% | 4.313817 | 52.172% | 0.113123 | 1.713836 | 0.302797 | 0.840898 | 82.624% |
| 2 | 0 | 196582.8 | 33.732% | 3.724277 | 58.708% | 0.090926 | 1.714731 | 0.370464 | 0.827099 | 80.183% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

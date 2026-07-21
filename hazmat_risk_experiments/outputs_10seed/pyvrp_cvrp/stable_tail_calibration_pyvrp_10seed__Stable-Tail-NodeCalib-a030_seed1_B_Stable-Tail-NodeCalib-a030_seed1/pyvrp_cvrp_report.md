# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 9.842212 | 0.000% | 0.307691 | 3.439235 | 0.256131 | 0.873263 | 89.859% |
| 0.25 | 0 | 155696.6 | 5.966% | 8.028836 | 18.424% | 0.248265 | 2.587739 | 0.221869 | 0.869571 | 88.567% |
| 0.5 | 0 | 163761.6 | 11.455% | 6.861012 | 30.290% | 0.206251 | 2.155998 | 0.226367 | 0.863874 | 87.312% |
| 1 | 0 | 173446.1 | 18.046% | 3.820440 | 61.183% | 0.081282 | 1.304134 | 0.245419 | 0.812368 | 78.637% |
| 2 | 0 | 187405.7 | 27.547% | 3.281837 | 66.655% | 0.064867 | 1.179503 | 0.250647 | 0.794370 | 75.493% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

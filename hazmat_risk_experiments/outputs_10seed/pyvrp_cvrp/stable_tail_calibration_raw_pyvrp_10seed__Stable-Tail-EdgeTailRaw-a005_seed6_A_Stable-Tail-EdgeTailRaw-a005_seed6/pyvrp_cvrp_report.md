# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.9 | 0.000% | 8.062251 | 0.000% | 0.238954 | 2.296755 | 0.156252 | 0.866593 | 88.709% |
| 0.25 | 0 | 143419.2 | 6.818% | 5.218183 | 35.276% | 0.149488 | 1.690659 | 0.232714 | 0.847205 | 85.592% |
| 0.5 | 0 | 149639.0 | 11.451% | 4.185689 | 48.083% | 0.123309 | 1.613083 | 0.316192 | 0.821454 | 82.209% |
| 1 | 0 | 158977.7 | 18.406% | 2.887451 | 64.186% | 0.077102 | 0.998139 | 0.289913 | 0.774979 | 75.407% |
| 2 | 0 | 173670.5 | 29.349% | 2.210746 | 72.579% | 0.050179 | 0.819862 | 0.285898 | 0.722237 | 68.207% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.437614 | 0.000% | 0.241984 | 2.788124 | 0.227106 | 0.865703 | 89.611% |
| 1 | 0 | 177770.3 | 21.154% | 3.712428 | 56.001% | 0.080774 | 1.379169 | 0.308276 | 0.815918 | 80.429% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

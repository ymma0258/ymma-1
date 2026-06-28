# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.910753 | 0.000% | 0.230922 | 2.602258 | 0.238660 | 0.879101 | 90.174% |
| 1 | 0 | 172997.0 | 17.741% | 2.740055 | 65.363% | 0.059111 | 0.918630 | 0.255911 | 0.793993 | 75.664% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

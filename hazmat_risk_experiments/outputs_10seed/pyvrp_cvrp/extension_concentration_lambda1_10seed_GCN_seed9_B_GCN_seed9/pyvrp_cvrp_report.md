# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.767275 | 0.000% | 0.244530 | 2.976577 | 0.243380 | 0.863051 | 89.308% |
| 1 | 0 | 178430.4 | 21.604% | 4.090628 | 53.342% | 0.110921 | 1.463062 | 0.312983 | 0.815907 | 81.526% |
| 1 | 1 | 194195.8 | 32.348% | 3.369818 | 61.564% | 0.084401 | 1.193241 | 0.285286 | 0.793948 | 77.555% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

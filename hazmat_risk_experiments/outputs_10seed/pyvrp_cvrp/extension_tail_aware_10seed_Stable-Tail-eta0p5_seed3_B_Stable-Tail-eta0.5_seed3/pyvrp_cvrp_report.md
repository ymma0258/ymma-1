# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.642772 | 0.000% | 0.164484 | 2.941509 | 0.216251 | 0.873089 | 88.794% |
| 1 | 0 | 174065.7 | 18.629% | 3.536813 | 59.078% | 0.058847 | 1.419896 | 0.289770 | 0.797031 | 76.373% |
| 2 | 0 | 189546.0 | 29.179% | 3.092456 | 64.219% | 0.050300 | 1.275780 | 0.322858 | 0.775073 | 73.186% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

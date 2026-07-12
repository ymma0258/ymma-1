# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 8.769583 | 0.000% | 0.276740 | 2.754712 | 0.204428 | 0.878420 | 89.189% |
| 0.25 | 0 | 157314.1 | 7.116% | 7.698563 | 12.213% | 0.210770 | 2.316154 | 0.207618 | 0.878405 | 89.673% |
| 0.5 | 0 | 166967.6 | 13.689% | 6.065823 | 30.831% | 0.168739 | 2.223002 | 0.286471 | 0.867016 | 87.425% |
| 1 | 0 | 179358.9 | 22.126% | 4.160389 | 52.559% | 0.112451 | 1.737570 | 0.322706 | 0.841986 | 82.980% |
| 2 | 0 | 199201.4 | 35.637% | 3.521526 | 59.844% | 0.088223 | 1.447289 | 0.327201 | 0.834660 | 80.720% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

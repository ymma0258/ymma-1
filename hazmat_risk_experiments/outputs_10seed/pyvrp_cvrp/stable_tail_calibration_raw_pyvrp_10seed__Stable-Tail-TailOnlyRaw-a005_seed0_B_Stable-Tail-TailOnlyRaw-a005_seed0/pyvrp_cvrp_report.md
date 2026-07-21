# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.4 | 0.000% | 7.601711 | 0.000% | 0.208738 | 2.532329 | 0.240727 | 0.878243 | 89.513% |
| 0.25 | 0 | 156807.3 | 6.432% | 6.407207 | 15.714% | 0.155887 | 2.260850 | 0.262585 | 0.872936 | 88.377% |
| 0.5 | 0 | 165502.6 | 12.334% | 4.687439 | 38.337% | 0.117988 | 1.562607 | 0.243947 | 0.850796 | 84.585% |
| 1 | 0 | 175733.7 | 19.279% | 3.110378 | 59.083% | 0.077766 | 1.159586 | 0.280969 | 0.810529 | 78.034% |
| 2 | 0 | 191219.2 | 29.789% | 2.406917 | 68.337% | 0.048322 | 0.893259 | 0.281796 | 0.775614 | 72.118% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

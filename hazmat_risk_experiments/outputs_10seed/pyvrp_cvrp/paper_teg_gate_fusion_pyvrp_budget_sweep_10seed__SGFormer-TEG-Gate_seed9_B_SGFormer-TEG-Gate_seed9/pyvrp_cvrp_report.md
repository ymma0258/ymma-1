# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 6.644939 | 0.000% | 0.196934 | 2.336776 | 0.270195 | 0.861967 | 86.252% |
| 0.25 | 0 | 154964.2 | 5.468% | 5.297858 | 20.272% | 0.136708 | 1.929327 | 0.255740 | 0.843335 | 83.121% |
| 0.5 | 0 | 160987.6 | 9.567% | 2.869398 | 56.818% | 0.058768 | 0.949291 | 0.183776 | 0.754367 | 70.536% |
| 1 | 0 | 167495.5 | 13.996% | 2.299712 | 65.392% | 0.044023 | 0.592405 | 0.131291 | 0.713688 | 64.729% |
| 2 | 0 | 178441.5 | 21.446% | 1.797894 | 72.943% | 0.030480 | 0.572272 | 0.217339 | 0.651008 | 55.820% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

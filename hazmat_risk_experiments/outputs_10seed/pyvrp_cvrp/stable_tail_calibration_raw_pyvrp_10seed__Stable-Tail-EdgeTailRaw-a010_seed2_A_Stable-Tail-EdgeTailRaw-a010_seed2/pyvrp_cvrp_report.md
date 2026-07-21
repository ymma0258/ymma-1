# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.4 | 0.000% | 9.069957 | 0.000% | 0.307925 | 2.690593 | 0.186239 | 0.880415 | 90.318% |
| 0.25 | 0 | 142300.8 | 6.091% | 5.974420 | 34.130% | 0.176634 | 2.195537 | 0.297753 | 0.867940 | 87.971% |
| 0.5 | 0 | 148383.3 | 10.625% | 4.866118 | 46.349% | 0.144636 | 1.836475 | 0.281479 | 0.854934 | 85.689% |
| 1 | 0 | 157012.5 | 17.059% | 3.261487 | 64.041% | 0.088053 | 1.233183 | 0.328697 | 0.812184 | 79.122% |
| 2 | 0 | 171323.9 | 27.728% | 2.901744 | 68.007% | 0.065378 | 1.212185 | 0.343396 | 0.796878 | 76.602% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

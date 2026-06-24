# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 6.883367 | 0.000% | 0.204340 | 2.370042 | 0.226137 | 0.873010 | 88.919% |
| 1 | 0 | 173995.4 | 18.581% | 2.945257 | 57.212% | 0.073990 | 1.154991 | 0.293761 | 0.801541 | 77.746% |
| 1 | 1 | 185936.1 | 26.719% | 2.350073 | 65.859% | 0.050131 | 0.851592 | 0.274595 | 0.775065 | 73.141% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

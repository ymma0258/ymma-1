# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 6.883367 | 0.000% | 0.204340 | 2.370042 | 0.226137 | 0.873010 | 88.919% |
| 0.25 | 0 | 155439.0 | 5.935% | 5.862332 | 14.833% | 0.145606 | 1.766188 | 0.222309 | 0.866404 | 87.916% |
| 0.5 | 0 | 163542.7 | 11.458% | 4.469013 | 35.075% | 0.115933 | 1.548960 | 0.224769 | 0.850124 | 84.602% |
| 1 | 0 | 173995.4 | 18.581% | 2.945257 | 57.212% | 0.073990 | 1.154991 | 0.293761 | 0.801541 | 77.746% |
| 2 | 0 | 189445.6 | 29.111% | 2.439098 | 64.565% | 0.054152 | 0.968557 | 0.306527 | 0.776501 | 73.598% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.0 | 0.000% | 6.840648 | 0.000% | 0.216189 | 2.184168 | 0.187502 | 0.866708 | 88.003% |
| 0.25 | 0 | 142005.1 | 5.660% | 4.988909 | 27.070% | 0.143384 | 1.514040 | 0.211330 | 0.858932 | 87.135% |
| 0.5 | 0 | 147455.3 | 9.715% | 3.639163 | 46.801% | 0.104579 | 1.214574 | 0.229413 | 0.833432 | 83.161% |
| 1 | 0 | 155733.1 | 15.875% | 2.351263 | 65.628% | 0.060213 | 0.737205 | 0.218382 | 0.767399 | 73.992% |
| 2 | 0 | 168322.1 | 25.242% | 2.157578 | 68.459% | 0.051798 | 0.702047 | 0.261404 | 0.754010 | 71.680% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

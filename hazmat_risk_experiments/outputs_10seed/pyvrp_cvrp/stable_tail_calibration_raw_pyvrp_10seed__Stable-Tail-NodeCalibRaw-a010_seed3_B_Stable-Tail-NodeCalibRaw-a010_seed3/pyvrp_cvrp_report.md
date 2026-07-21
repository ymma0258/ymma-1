# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.7 | 0.000% | 6.966378 | 0.000% | 0.191473 | 2.529693 | 0.271913 | 0.867542 | 88.920% |
| 0.25 | 0 | 155562.8 | 5.587% | 5.649014 | 18.910% | 0.140835 | 1.965596 | 0.247353 | 0.864046 | 87.751% |
| 0.5 | 0 | 163357.5 | 10.878% | 4.771910 | 31.501% | 0.121070 | 1.807165 | 0.261488 | 0.853746 | 85.858% |
| 1 | 0 | 175679.1 | 19.241% | 3.589966 | 48.467% | 0.095611 | 1.417158 | 0.303113 | 0.835522 | 82.048% |
| 2 | 0 | 192774.8 | 30.845% | 2.715663 | 61.018% | 0.067824 | 1.088272 | 0.290798 | 0.807952 | 77.207% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

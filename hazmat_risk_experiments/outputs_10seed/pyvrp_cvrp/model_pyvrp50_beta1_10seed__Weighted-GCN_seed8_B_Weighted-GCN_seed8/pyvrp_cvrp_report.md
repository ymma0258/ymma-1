# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.929044 | 0.000% | 0.224611 | 2.504852 | 0.195410 | 0.833668 | 85.640% |
| 1 | 0 | 178266.5 | 21.492% | 3.939511 | 50.315% | 0.083887 | 1.547731 | 0.278939 | 0.739961 | 73.841% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

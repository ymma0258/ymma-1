# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 6.837082 | 0.000% | 0.203132 | 2.183778 | 0.187969 | 0.829465 | 85.050% |
| 1 | 0 | 173478.2 | 18.229% | 3.059502 | 55.251% | 0.060078 | 0.961160 | 0.204136 | 0.688856 | 67.802% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

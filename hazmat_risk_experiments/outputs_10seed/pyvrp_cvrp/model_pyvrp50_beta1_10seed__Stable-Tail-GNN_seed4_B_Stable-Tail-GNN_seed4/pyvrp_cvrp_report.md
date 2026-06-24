# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.275491 | 0.000% | 0.291917 | 3.021439 | 0.209019 | 0.877111 | 89.848% |
| 1 | 0 | 176959.2 | 20.601% | 3.963414 | 57.270% | 0.094040 | 1.577595 | 0.340760 | 0.821793 | 80.036% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

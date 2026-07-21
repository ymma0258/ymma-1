# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 6.300825 | 0.000% | 0.183062 | 1.779218 | 0.148005 | 0.865900 | 88.600% |
| 0.25 | 0 | 143174.7 | 6.848% | 4.076425 | 35.303% | 0.118599 | 1.374106 | 0.255593 | 0.846833 | 85.376% |
| 0.5 | 0 | 149198.7 | 11.344% | 3.223647 | 48.838% | 0.094133 | 1.180961 | 0.295181 | 0.818605 | 81.737% |
| 1 | 0 | 158690.6 | 18.428% | 2.300475 | 63.489% | 0.061435 | 0.719523 | 0.254901 | 0.778570 | 75.936% |
| 2 | 0 | 173140.4 | 29.211% | 1.794084 | 71.526% | 0.040817 | 0.653558 | 0.293929 | 0.724971 | 68.563% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

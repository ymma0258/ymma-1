# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.325140 | 0.000% | 0.252710 | 2.391842 | 0.135789 | 0.848338 | 87.650% |
| 1 | 0 | 161899.6 | 20.823% | 3.662661 | 56.005% | 0.088346 | 1.219682 | 0.275593 | 0.755859 | 74.995% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

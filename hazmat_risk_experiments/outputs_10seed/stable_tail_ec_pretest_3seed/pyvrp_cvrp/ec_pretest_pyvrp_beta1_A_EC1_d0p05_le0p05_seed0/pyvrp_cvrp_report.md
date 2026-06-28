# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.143877 | 0.000% | 0.261577 | 2.314103 | 0.149125 | 0.862630 | 89.445% |
| 1 | 0 | 161420.1 | 20.465% | 3.288831 | 59.616% | 0.076447 | 0.941951 | 0.196679 | 0.801288 | 78.966% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

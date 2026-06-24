# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.721826 | 0.000% | 0.273831 | 2.603956 | 0.158552 | 0.858604 | 88.998% |
| 1 | 0 | 159937.1 | 19.358% | 3.749809 | 57.007% | 0.083890 | 1.126321 | 0.221557 | 0.781726 | 77.801% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 17.325762 | 0.000% | 0.159415 | 5.309906 | 0.192689 | 0.833684 | 88.873% |
| 1 | 0 | 186348.0 | 27.443% | 10.281482 | 40.658% | 0.107250 | 3.417028 | 0.255420 | 0.801400 | 82.824% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

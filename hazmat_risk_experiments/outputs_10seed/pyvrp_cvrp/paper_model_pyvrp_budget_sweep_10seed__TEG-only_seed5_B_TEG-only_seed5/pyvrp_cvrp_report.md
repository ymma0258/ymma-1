# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.8 | 0.000% | 8.085176 | 0.000% | 0.232136 | 2.466857 | 0.194320 | 0.823568 | 85.564% |
| 0.25 | 0 | 157212.7 | 6.852% | 7.048423 | 12.823% | 0.198208 | 2.198865 | 0.191841 | 0.816084 | 84.383% |
| 0.5 | 0 | 166359.7 | 13.069% | 5.546960 | 31.393% | 0.126173 | 1.557430 | 0.183295 | 0.787969 | 80.497% |
| 1 | 0 | 178445.0 | 21.283% | 4.293320 | 46.899% | 0.089377 | 1.323750 | 0.214654 | 0.736746 | 74.621% |
| 2 | 0 | 198004.6 | 34.577% | 3.461569 | 57.186% | 0.069782 | 1.085452 | 0.226856 | 0.690465 | 68.400% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

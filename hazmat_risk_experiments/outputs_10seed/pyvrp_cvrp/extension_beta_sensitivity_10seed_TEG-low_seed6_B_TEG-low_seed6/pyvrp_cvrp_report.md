# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146797.4 | 0.000% | 8.689805 | 0.000% | 0.258968 | 2.816329 | 0.214173 | 0.843276 | 87.073% |
| 0.5 | 0 | 166814.1 | 13.636% | 6.235971 | 28.238% | 0.172858 | 1.840767 | 0.203237 | 0.822709 | 83.424% |
| 1 | 0 | 180103.9 | 22.689% | 4.386909 | 49.517% | 0.091800 | 1.457833 | 0.285867 | 0.773276 | 76.681% |
| 1.5 | 0 | 190255.0 | 29.604% | 3.723747 | 57.148% | 0.073953 | 1.400934 | 0.300873 | 0.747650 | 72.979% |
| 2 | 0 | 199666.4 | 36.015% | 3.551020 | 59.136% | 0.069815 | 1.395041 | 0.311354 | 0.736973 | 71.604% |
| 3 | 0 | 217460.3 | 48.136% | 3.339926 | 61.565% | 0.065068 | 1.320398 | 0.316302 | 0.728602 | 70.112% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

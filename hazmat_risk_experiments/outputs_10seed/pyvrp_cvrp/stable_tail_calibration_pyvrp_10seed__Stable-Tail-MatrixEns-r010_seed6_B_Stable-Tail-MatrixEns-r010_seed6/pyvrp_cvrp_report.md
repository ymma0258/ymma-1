# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.975549 | 0.000% | 0.239768 | 2.615248 | 0.217249 | 0.868876 | 89.106% |
| 0.25 | 0 | 157650.5 | 7.296% | 7.037141 | 11.766% | 0.177354 | 2.373912 | 0.232140 | 0.867674 | 89.227% |
| 0.5 | 0 | 168287.7 | 14.536% | 5.298462 | 33.566% | 0.135508 | 1.612962 | 0.213112 | 0.853870 | 86.118% |
| 1 | 0 | 181452.0 | 23.495% | 3.711383 | 53.465% | 0.093270 | 1.442272 | 0.341566 | 0.825654 | 81.008% |
| 2 | 0 | 202420.1 | 37.766% | 3.346967 | 58.035% | 0.085969 | 1.242898 | 0.328991 | 0.815752 | 79.064% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

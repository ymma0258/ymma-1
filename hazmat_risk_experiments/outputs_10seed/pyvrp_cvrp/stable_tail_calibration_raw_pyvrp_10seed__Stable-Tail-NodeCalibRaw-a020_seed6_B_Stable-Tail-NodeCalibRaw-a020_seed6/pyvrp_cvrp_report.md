# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.4 | 0.000% | 8.940983 | 0.000% | 0.233406 | 3.095847 | 0.243831 | 0.869550 | 89.367% |
| 0.25 | 0 | 158056.4 | 7.377% | 7.849101 | 12.212% | 0.192834 | 2.505730 | 0.226385 | 0.869976 | 89.280% |
| 0.5 | 0 | 168693.6 | 14.604% | 6.038980 | 32.457% | 0.155752 | 1.998220 | 0.230625 | 0.855821 | 86.350% |
| 1 | 0 | 181942.5 | 23.604% | 4.404315 | 50.740% | 0.114896 | 1.657272 | 0.313867 | 0.829701 | 81.791% |
| 2 | 0 | 203688.5 | 38.378% | 3.769501 | 57.840% | 0.094870 | 1.333712 | 0.324749 | 0.817489 | 79.151% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

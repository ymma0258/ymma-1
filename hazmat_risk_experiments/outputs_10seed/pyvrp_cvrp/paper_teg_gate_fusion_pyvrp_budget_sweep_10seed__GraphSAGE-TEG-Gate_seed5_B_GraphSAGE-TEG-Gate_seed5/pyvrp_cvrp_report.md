# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.613231 | 0.000% | 0.212311 | 2.410167 | 0.198427 | 0.880382 | 89.532% |
| 0.25 | 0 | 158003.7 | 7.536% | 6.816253 | 10.468% | 0.174030 | 2.080786 | 0.178965 | 0.879929 | 89.500% |
| 0.5 | 0 | 167692.4 | 14.130% | 4.967681 | 34.749% | 0.129182 | 1.690738 | 0.257303 | 0.862648 | 86.103% |
| 1 | 0 | 180003.6 | 22.509% | 3.159981 | 58.494% | 0.079682 | 1.112255 | 0.312280 | 0.827539 | 79.589% |
| 2 | 0 | 197962.6 | 34.732% | 2.762889 | 63.709% | 0.065489 | 0.957480 | 0.312344 | 0.810205 | 76.766% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

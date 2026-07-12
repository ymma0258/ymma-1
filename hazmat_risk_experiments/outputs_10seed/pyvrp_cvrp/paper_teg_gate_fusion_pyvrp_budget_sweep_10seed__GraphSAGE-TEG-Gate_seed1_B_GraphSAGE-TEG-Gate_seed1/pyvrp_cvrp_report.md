# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 10.472055 | 0.000% | 0.329665 | 3.601244 | 0.245091 | 0.882749 | 90.829% |
| 0.25 | 0 | 155647.6 | 5.885% | 8.223916 | 21.468% | 0.256253 | 2.261244 | 0.174770 | 0.879676 | 89.199% |
| 0.5 | 0 | 163931.9 | 11.520% | 6.661016 | 36.392% | 0.194572 | 2.266167 | 0.261194 | 0.868262 | 87.028% |
| 1 | 0 | 173167.7 | 17.803% | 3.793860 | 63.772% | 0.081385 | 1.198030 | 0.233990 | 0.827407 | 79.231% |
| 2 | 0 | 185802.0 | 26.398% | 2.999085 | 71.361% | 0.061232 | 1.053619 | 0.253808 | 0.796932 | 73.854% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

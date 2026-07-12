# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.9 | 0.000% | 8.640140 | 0.000% | 0.234866 | 2.652782 | 0.185133 | 0.871373 | 88.857% |
| 0.25 | 0 | 157560.3 | 7.089% | 7.175189 | 16.955% | 0.181210 | 2.406061 | 0.222780 | 0.866040 | 87.793% |
| 0.5 | 0 | 166068.6 | 12.871% | 4.631770 | 46.392% | 0.112842 | 1.415783 | 0.199956 | 0.823729 | 81.434% |
| 1 | 0 | 175537.3 | 19.307% | 3.126586 | 63.813% | 0.073899 | 0.975937 | 0.222984 | 0.779841 | 74.092% |
| 2 | 0 | 190515.8 | 29.487% | 2.710373 | 68.630% | 0.060231 | 0.946840 | 0.247284 | 0.763625 | 71.143% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

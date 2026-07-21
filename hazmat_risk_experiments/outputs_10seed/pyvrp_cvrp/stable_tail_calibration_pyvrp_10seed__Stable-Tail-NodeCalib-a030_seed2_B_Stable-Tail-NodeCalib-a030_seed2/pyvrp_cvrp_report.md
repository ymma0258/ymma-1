# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 8.990715 | 0.000% | 0.282061 | 3.477741 | 0.315252 | 0.875172 | 89.571% |
| 0.25 | 0 | 156473.1 | 6.543% | 7.610873 | 15.347% | 0.226181 | 3.152693 | 0.339017 | 0.872325 | 88.822% |
| 0.5 | 0 | 164650.0 | 12.111% | 6.400137 | 28.814% | 0.192387 | 2.398645 | 0.288384 | 0.861119 | 86.956% |
| 1 | 0 | 177172.2 | 20.637% | 4.390268 | 51.169% | 0.114270 | 1.656123 | 0.278186 | 0.840289 | 82.780% |
| 2 | 0 | 195861.0 | 33.362% | 3.696424 | 58.886% | 0.089851 | 1.715188 | 0.390384 | 0.829637 | 80.450% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

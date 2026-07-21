# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.4 | 0.000% | 8.403493 | 0.000% | 0.262600 | 2.381373 | 0.154185 | 0.860553 | 88.177% |
| 0.25 | 0 | 142400.1 | 6.165% | 5.628082 | 33.027% | 0.175129 | 1.643567 | 0.179327 | 0.843321 | 86.084% |
| 0.5 | 0 | 148376.7 | 10.620% | 4.549306 | 45.864% | 0.135155 | 1.658784 | 0.259508 | 0.823729 | 83.422% |
| 1 | 0 | 156732.6 | 16.850% | 2.959702 | 64.780% | 0.061934 | 1.023251 | 0.254821 | 0.756105 | 74.236% |
| 2 | 0 | 169900.4 | 26.667% | 2.501697 | 70.230% | 0.052039 | 0.853739 | 0.248834 | 0.730161 | 70.270% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

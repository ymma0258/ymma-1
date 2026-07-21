# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 9.257467 | 0.000% | 0.298012 | 2.705313 | 0.161031 | 0.872971 | 89.455% |
| 0.25 | 0 | 142066.8 | 5.759% | 6.534933 | 29.409% | 0.199626 | 1.901546 | 0.175332 | 0.865342 | 87.950% |
| 0.5 | 0 | 148124.3 | 10.268% | 4.855666 | 47.549% | 0.128601 | 1.698770 | 0.252385 | 0.845993 | 84.533% |
| 1 | 0 | 156491.2 | 16.496% | 3.269649 | 64.681% | 0.072203 | 1.083709 | 0.235791 | 0.793932 | 77.132% |
| 2 | 0 | 169629.2 | 26.277% | 2.713152 | 70.692% | 0.057127 | 0.824415 | 0.233028 | 0.770582 | 73.163% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

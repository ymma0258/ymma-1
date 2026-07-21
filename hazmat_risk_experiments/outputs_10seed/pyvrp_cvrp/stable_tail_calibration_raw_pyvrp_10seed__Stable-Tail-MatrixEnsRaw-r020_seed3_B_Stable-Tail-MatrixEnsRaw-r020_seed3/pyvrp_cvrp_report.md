# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 5.511598 | 0.000% | 0.164180 | 1.817083 | 0.235610 | 0.869074 | 88.877% |
| 0.25 | 0 | 155436.7 | 5.645% | 4.727212 | 14.232% | 0.118617 | 1.746726 | 0.269202 | 0.863869 | 87.940% |
| 0.5 | 0 | 162941.1 | 10.746% | 3.821336 | 30.667% | 0.096477 | 1.486412 | 0.257138 | 0.853745 | 85.863% |
| 1 | 0 | 174575.7 | 18.654% | 2.722553 | 50.603% | 0.072038 | 1.117511 | 0.307980 | 0.834580 | 81.679% |
| 2 | 0 | 191783.6 | 30.349% | 2.182226 | 60.407% | 0.054302 | 0.884941 | 0.300522 | 0.806360 | 77.067% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 7.164918 | 0.000% | 0.220444 | 2.036974 | 0.164985 | 0.872055 | 88.704% |
| 0.25 | 0 | 142420.2 | 6.232% | 5.215850 | 27.203% | 0.151573 | 1.802694 | 0.254039 | 0.862198 | 86.739% |
| 0.5 | 0 | 148015.5 | 10.406% | 3.560850 | 50.302% | 0.104283 | 1.401347 | 0.322169 | 0.826943 | 81.431% |
| 1 | 0 | 156187.9 | 16.502% | 2.489728 | 65.251% | 0.064257 | 0.970619 | 0.279681 | 0.768911 | 73.204% |
| 2 | 0 | 167472.6 | 24.919% | 1.915292 | 73.268% | 0.041703 | 0.624041 | 0.218954 | 0.718431 | 65.991% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

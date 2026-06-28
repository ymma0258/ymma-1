# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.339548 | 0.000% | 0.242076 | 2.653866 | 0.207785 | 0.836548 | 86.597% |
| 0.5 | 0 | 165081.5 | 12.506% | 5.133472 | 38.444% | 0.111257 | 1.414439 | 0.166089 | 0.782798 | 79.542% |
| 1 | 0 | 176257.9 | 20.123% | 3.953627 | 52.592% | 0.078281 | 1.184048 | 0.191167 | 0.738341 | 73.969% |
| 1.5 | 0 | 185674.0 | 26.540% | 3.420038 | 58.990% | 0.066323 | 1.089870 | 0.231853 | 0.710358 | 70.160% |
| 2 | 0 | 193715.7 | 32.021% | 3.040933 | 63.536% | 0.057160 | 1.030810 | 0.247025 | 0.680632 | 66.421% |
| 3 | 0 | 208326.3 | 41.978% | 2.923068 | 64.949% | 0.053697 | 1.013155 | 0.251827 | 0.669869 | 65.052% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

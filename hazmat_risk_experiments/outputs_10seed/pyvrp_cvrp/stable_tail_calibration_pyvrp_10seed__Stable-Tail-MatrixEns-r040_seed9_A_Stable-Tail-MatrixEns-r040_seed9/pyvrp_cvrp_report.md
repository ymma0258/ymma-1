# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 4.891383 | 0.000% | 0.153180 | 1.469784 | 0.169549 | 0.870801 | 89.629% |
| 0.25 | 0 | 142852.1 | 6.608% | 3.542703 | 27.573% | 0.101759 | 1.046956 | 0.184471 | 0.859618 | 87.589% |
| 0.5 | 0 | 148930.8 | 11.144% | 2.693507 | 44.934% | 0.060276 | 1.186289 | 0.313703 | 0.832490 | 84.114% |
| 1 | 0 | 157680.0 | 17.674% | 1.766557 | 63.884% | 0.039852 | 0.633872 | 0.249494 | 0.778428 | 76.370% |
| 2 | 0 | 171140.5 | 27.719% | 1.461695 | 70.117% | 0.033528 | 0.424368 | 0.225741 | 0.747532 | 71.822% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

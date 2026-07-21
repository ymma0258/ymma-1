# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.9 | 0.000% | 5.688016 | 0.000% | 0.174595 | 1.852904 | 0.223343 | 0.877014 | 89.527% |
| 0.25 | 0 | 156279.6 | 6.122% | 4.887544 | 14.073% | 0.126538 | 1.501418 | 0.199994 | 0.876182 | 89.132% |
| 0.5 | 0 | 164781.5 | 11.895% | 3.939783 | 30.735% | 0.095679 | 1.347001 | 0.260208 | 0.856748 | 86.036% |
| 1 | 0 | 174956.7 | 18.805% | 2.442098 | 57.066% | 0.060624 | 0.902600 | 0.308256 | 0.821125 | 79.832% |
| 2 | 0 | 190510.2 | 29.367% | 1.965003 | 65.454% | 0.047797 | 0.605892 | 0.268948 | 0.794727 | 75.328% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

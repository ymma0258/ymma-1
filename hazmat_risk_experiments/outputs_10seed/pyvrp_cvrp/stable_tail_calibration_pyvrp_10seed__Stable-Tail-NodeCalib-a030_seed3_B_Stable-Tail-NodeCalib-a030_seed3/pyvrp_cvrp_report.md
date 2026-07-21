# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 6.987902 | 0.000% | 0.191153 | 2.344865 | 0.244591 | 0.869505 | 88.898% |
| 0.25 | 0 | 155143.3 | 5.542% | 5.771786 | 17.403% | 0.144287 | 2.031789 | 0.275424 | 0.863690 | 87.866% |
| 0.5 | 0 | 162989.2 | 10.879% | 4.710016 | 32.598% | 0.119659 | 1.833878 | 0.273670 | 0.853261 | 85.611% |
| 1 | 0 | 174825.3 | 18.931% | 3.434479 | 50.851% | 0.091205 | 1.408203 | 0.311988 | 0.834885 | 81.814% |
| 2 | 0 | 192042.9 | 30.644% | 2.728723 | 60.951% | 0.068368 | 1.093060 | 0.291739 | 0.808741 | 77.353% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 7.712965 | 0.000% | 0.232754 | 2.675041 | 0.252832 | 0.859204 | 89.101% |
| 1 | 0 | 179227.6 | 22.314% | 3.678792 | 52.304% | 0.091462 | 1.321969 | 0.329059 | 0.813603 | 80.999% |
| 1 | 0.5 | 187206.6 | 27.759% | 3.093937 | 59.887% | 0.073869 | 0.886212 | 0.204800 | 0.787548 | 77.097% |
| 1 | 1 | 194023.8 | 32.411% | 2.833941 | 63.257% | 0.064309 | 0.857136 | 0.242997 | 0.770729 | 74.532% |
| 1 | 2 | 206812.4 | 41.139% | 2.675827 | 65.307% | 0.059280 | 0.856890 | 0.263044 | 0.761463 | 73.051% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

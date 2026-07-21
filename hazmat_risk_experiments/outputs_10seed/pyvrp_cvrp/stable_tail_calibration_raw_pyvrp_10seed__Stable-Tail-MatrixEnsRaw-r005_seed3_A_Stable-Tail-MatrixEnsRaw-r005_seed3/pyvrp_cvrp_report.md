# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 6.658933 | 0.000% | 0.202079 | 2.041768 | 0.185147 | 0.871421 | 88.809% |
| 0.25 | 0 | 141869.7 | 5.717% | 4.421492 | 33.601% | 0.125450 | 1.350805 | 0.201760 | 0.852830 | 86.268% |
| 0.5 | 0 | 147361.8 | 9.809% | 3.546058 | 46.747% | 0.099310 | 1.167519 | 0.218341 | 0.835718 | 83.489% |
| 1 | 0 | 155346.9 | 15.759% | 2.297785 | 65.493% | 0.059771 | 0.733637 | 0.246828 | 0.770684 | 74.478% |
| 2 | 0 | 167562.6 | 24.862% | 2.014678 | 69.745% | 0.049065 | 0.663434 | 0.252281 | 0.749522 | 71.123% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

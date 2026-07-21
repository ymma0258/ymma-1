# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 7.264112 | 0.000% | 0.234117 | 2.005801 | 0.143788 | 0.872429 | 89.655% |
| 0.25 | 0 | 141903.3 | 5.899% | 5.272789 | 27.413% | 0.161929 | 1.583232 | 0.192947 | 0.867158 | 88.227% |
| 0.5 | 0 | 147784.5 | 10.289% | 3.872648 | 46.688% | 0.103840 | 1.484451 | 0.268191 | 0.842403 | 84.310% |
| 1 | 0 | 156308.4 | 16.650% | 2.688026 | 62.996% | 0.057947 | 0.849480 | 0.194490 | 0.797491 | 77.659% |
| 2 | 0 | 169239.6 | 26.300% | 2.212498 | 69.542% | 0.043822 | 0.654488 | 0.210979 | 0.775102 | 73.689% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

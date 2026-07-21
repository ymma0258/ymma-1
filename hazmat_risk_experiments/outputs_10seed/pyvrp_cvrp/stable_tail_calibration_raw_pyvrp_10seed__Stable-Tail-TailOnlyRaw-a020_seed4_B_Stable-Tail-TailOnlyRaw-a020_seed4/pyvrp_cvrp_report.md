# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147396.8 | 0.000% | 9.292535 | 0.000% | 0.290679 | 3.186696 | 0.236452 | 0.879590 | 90.042% |
| 0.25 | 0 | 156785.7 | 6.370% | 7.726926 | 16.848% | 0.214882 | 2.415476 | 0.215168 | 0.878111 | 89.061% |
| 0.5 | 0 | 164497.9 | 11.602% | 5.986790 | 35.574% | 0.157344 | 2.079154 | 0.281710 | 0.860391 | 86.055% |
| 1 | 0 | 175022.6 | 18.742% | 4.041950 | 56.503% | 0.102569 | 1.601684 | 0.326753 | 0.828139 | 80.814% |
| 2 | 0 | 190995.6 | 29.579% | 3.338971 | 64.068% | 0.068346 | 1.362781 | 0.354767 | 0.807383 | 77.565% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134531.2 | 0.000% | 8.629230 | 0.000% | 0.270644 | 2.598752 | 0.194945 | 0.886433 | 90.907% |
| 0.25 | 0 | 142236.7 | 5.728% | 5.054119 | 41.430% | 0.153108 | 1.628893 | 0.222347 | 0.869402 | 87.390% |
| 0.5 | 0 | 147804.4 | 9.866% | 4.047742 | 53.093% | 0.122208 | 1.559176 | 0.303783 | 0.851816 | 84.974% |
| 1 | 0 | 155523.6 | 15.604% | 2.616909 | 69.674% | 0.064380 | 1.099287 | 0.296845 | 0.797165 | 76.921% |
| 2 | 0 | 166697.4 | 23.910% | 1.944484 | 77.466% | 0.036245 | 0.655083 | 0.246013 | 0.746124 | 68.899% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

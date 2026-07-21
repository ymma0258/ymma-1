# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147396.9 | 0.000% | 7.204648 | 0.000% | 0.203433 | 2.427024 | 0.250911 | 0.869870 | 89.053% |
| 0.25 | 0 | 155478.0 | 5.483% | 5.648582 | 21.598% | 0.141108 | 2.130937 | 0.264194 | 0.863088 | 87.587% |
| 0.5 | 0 | 163324.3 | 10.806% | 4.728923 | 34.363% | 0.121165 | 1.735781 | 0.239095 | 0.853815 | 85.730% |
| 1 | 0 | 175218.8 | 18.875% | 3.687881 | 48.812% | 0.099647 | 1.466965 | 0.295407 | 0.839672 | 82.640% |
| 2 | 0 | 193263.4 | 31.118% | 2.862377 | 60.270% | 0.072725 | 1.203242 | 0.299303 | 0.815061 | 78.342% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

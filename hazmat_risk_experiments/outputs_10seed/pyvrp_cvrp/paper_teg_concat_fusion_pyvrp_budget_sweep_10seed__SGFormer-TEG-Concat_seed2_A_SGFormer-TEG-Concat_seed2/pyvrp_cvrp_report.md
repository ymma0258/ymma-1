# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.7 | 0.000% | 9.150724 | 0.000% | 0.296496 | 2.630653 | 0.155188 | 0.872437 | 89.457% |
| 0.25 | 0 | 143405.8 | 6.755% | 5.748944 | 37.175% | 0.169548 | 1.922281 | 0.255037 | 0.862107 | 86.116% |
| 0.5 | 0 | 149945.5 | 11.623% | 4.630682 | 49.395% | 0.122907 | 1.709035 | 0.285986 | 0.845807 | 83.306% |
| 1 | 0 | 158926.1 | 18.309% | 3.068940 | 66.462% | 0.066774 | 1.060779 | 0.305176 | 0.796139 | 75.479% |
| 2 | 0 | 173496.2 | 29.155% | 2.714706 | 70.333% | 0.054058 | 1.071393 | 0.290138 | 0.777206 | 72.243% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

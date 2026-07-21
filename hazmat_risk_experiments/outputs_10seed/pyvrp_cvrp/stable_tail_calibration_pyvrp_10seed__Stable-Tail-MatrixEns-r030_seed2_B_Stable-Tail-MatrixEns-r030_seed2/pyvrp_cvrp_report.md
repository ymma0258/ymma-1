# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 6.194214 | 0.000% | 0.192377 | 2.346478 | 0.307074 | 0.874725 | 89.573% |
| 0.25 | 0 | 156437.8 | 6.471% | 5.079212 | 18.001% | 0.155527 | 1.948770 | 0.315038 | 0.869325 | 88.431% |
| 0.5 | 0 | 165293.7 | 12.498% | 4.489068 | 27.528% | 0.124582 | 1.806212 | 0.311981 | 0.864813 | 87.411% |
| 1 | 0 | 177354.0 | 20.706% | 3.051179 | 50.741% | 0.082044 | 1.195310 | 0.293279 | 0.841851 | 82.960% |
| 2 | 0 | 196394.7 | 33.665% | 2.548176 | 58.862% | 0.064040 | 1.131569 | 0.363112 | 0.828577 | 80.406% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.6 | 0.000% | 8.817944 | 0.000% | 0.297071 | 2.686092 | 0.191231 | 0.878109 | 90.019% |
| 0.25 | 0 | 142371.2 | 6.143% | 5.614584 | 36.328% | 0.164846 | 2.060146 | 0.274218 | 0.862532 | 87.246% |
| 0.5 | 0 | 148468.0 | 10.688% | 4.587723 | 47.973% | 0.138702 | 1.383706 | 0.205742 | 0.853366 | 85.107% |
| 1 | 0 | 157571.3 | 17.475% | 3.233410 | 63.331% | 0.084770 | 1.220453 | 0.346612 | 0.812151 | 79.080% |
| 2 | 0 | 172152.5 | 28.346% | 2.851303 | 67.665% | 0.068278 | 1.192248 | 0.349786 | 0.792218 | 75.946% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

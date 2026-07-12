# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 8.393970 | 0.000% | 0.247031 | 2.506540 | 0.179248 | 0.879552 | 89.998% |
| 0.25 | 0 | 158950.6 | 8.034% | 7.446779 | 11.284% | 0.204881 | 2.380004 | 0.219847 | 0.877038 | 89.309% |
| 0.5 | 0 | 168780.1 | 14.714% | 4.944029 | 41.100% | 0.127581 | 2.003560 | 0.341653 | 0.853732 | 84.793% |
| 1 | 0 | 181354.1 | 23.261% | 3.576628 | 57.391% | 0.078463 | 1.369307 | 0.311950 | 0.828534 | 80.156% |
| 2 | 0 | 201206.5 | 36.754% | 2.874796 | 65.752% | 0.060631 | 1.076913 | 0.307624 | 0.794679 | 74.613% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

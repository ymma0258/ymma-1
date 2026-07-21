# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 4.256280 | 0.000% | 0.133067 | 1.458420 | 0.245334 | 0.870307 | 89.066% |
| 0.25 | 0 | 155055.9 | 5.578% | 3.440244 | 19.173% | 0.086256 | 1.193204 | 0.273915 | 0.864900 | 87.882% |
| 0.5 | 0 | 162853.7 | 10.887% | 2.809473 | 33.992% | 0.070309 | 1.107159 | 0.286141 | 0.852316 | 85.484% |
| 1 | 0 | 174331.7 | 18.703% | 2.149073 | 49.508% | 0.055277 | 0.838290 | 0.297200 | 0.839406 | 82.406% |
| 2 | 0 | 191463.5 | 30.368% | 1.611393 | 62.141% | 0.040252 | 0.656868 | 0.293530 | 0.804479 | 76.735% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 10.641821 | 0.000% | 0.261624 | 3.113351 | 0.168884 | 0.854840 | 88.738% |
| 1.5 | 1 | 180287.6 | 34.545% | 2.837783 | 73.334% | 0.047812 | 1.111919 | 0.294213 | 0.664769 | 63.502% |
| 2 | 1 | 186789.8 | 39.398% | 2.763176 | 74.035% | 0.044928 | 1.123875 | 0.286049 | 0.656901 | 62.508% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

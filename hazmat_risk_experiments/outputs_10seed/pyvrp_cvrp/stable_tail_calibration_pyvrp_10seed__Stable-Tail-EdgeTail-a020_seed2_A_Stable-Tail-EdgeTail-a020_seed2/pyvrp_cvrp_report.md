# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 9.186934 | 0.000% | 0.298801 | 2.638608 | 0.170278 | 0.881888 | 90.459% |
| 0.25 | 0 | 142304.3 | 6.146% | 6.096804 | 33.636% | 0.179459 | 2.129465 | 0.259769 | 0.869511 | 88.062% |
| 0.5 | 0 | 148279.0 | 10.603% | 4.829673 | 47.429% | 0.144735 | 1.764922 | 0.269094 | 0.856311 | 85.700% |
| 1 | 0 | 157256.6 | 17.299% | 3.334422 | 63.705% | 0.090809 | 1.347990 | 0.324549 | 0.816493 | 79.650% |
| 2 | 0 | 171177.1 | 27.683% | 2.972237 | 67.647% | 0.076164 | 1.282560 | 0.367898 | 0.798810 | 76.846% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

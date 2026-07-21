# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 6.282314 | 0.000% | 0.193462 | 1.765368 | 0.153351 | 0.879721 | 90.334% |
| 0.25 | 0 | 143144.3 | 6.826% | 4.829501 | 23.125% | 0.150306 | 1.549608 | 0.256514 | 0.874530 | 89.139% |
| 0.5 | 0 | 149922.0 | 11.884% | 3.495264 | 44.363% | 0.106157 | 1.204449 | 0.268927 | 0.851862 | 85.502% |
| 1 | 0 | 159190.2 | 18.800% | 2.467138 | 60.729% | 0.065244 | 0.724260 | 0.239250 | 0.819159 | 80.286% |
| 2 | 0 | 174063.1 | 29.900% | 2.019342 | 67.857% | 0.048463 | 0.740458 | 0.339224 | 0.792530 | 76.274% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.764525 | 0.000% | 0.284438 | 3.273121 | 0.245837 | 0.843413 | 88.250% |
| 0.5 | 0 | 166396.8 | 13.403% | 5.898773 | 39.590% | 0.162172 | 2.028556 | 0.245660 | 0.804280 | 81.997% |
| 1 | 0 | 179410.9 | 22.272% | 4.942771 | 49.380% | 0.100676 | 1.772606 | 0.264403 | 0.782497 | 78.958% |
| 1.5 | 0 | 190123.3 | 29.573% | 4.093123 | 58.082% | 0.082385 | 1.604403 | 0.292230 | 0.745762 | 74.104% |
| 2 | 0 | 198783.2 | 35.475% | 3.761303 | 61.480% | 0.073323 | 1.510065 | 0.301784 | 0.729049 | 71.899% |
| 3 | 0 | 215412.4 | 46.808% | 3.617124 | 62.956% | 0.071064 | 1.538548 | 0.328605 | 0.722215 | 70.926% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.0 | 0.000% | 8.785374 | 0.000% | 0.289319 | 2.619595 | 0.183663 | 0.870023 | 89.284% |
| 0.25 | 0 | 143329.1 | 6.645% | 5.488852 | 37.523% | 0.170081 | 1.864493 | 0.245424 | 0.851793 | 86.664% |
| 0.5 | 0 | 149718.8 | 11.400% | 4.549215 | 48.218% | 0.136355 | 1.707279 | 0.270614 | 0.830776 | 84.072% |
| 1 | 0 | 158588.8 | 17.999% | 2.992378 | 65.939% | 0.074544 | 1.043737 | 0.237371 | 0.778884 | 76.410% |
| 2 | 0 | 172860.9 | 28.619% | 2.466145 | 71.929% | 0.054066 | 0.752905 | 0.218152 | 0.747617 | 71.818% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

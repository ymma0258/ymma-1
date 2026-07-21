# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 7.120352 | 0.000% | 0.219457 | 2.105999 | 0.166254 | 0.870576 | 88.468% |
| 0.25 | 0 | 142252.1 | 6.160% | 5.543567 | 22.145% | 0.160290 | 1.809565 | 0.237293 | 0.865469 | 87.371% |
| 0.5 | 0 | 147919.5 | 10.389% | 3.544108 | 50.226% | 0.102094 | 1.339877 | 0.319338 | 0.825464 | 81.139% |
| 1 | 0 | 155806.7 | 16.275% | 2.478249 | 65.195% | 0.064581 | 0.958321 | 0.282199 | 0.769786 | 73.378% |
| 2 | 0 | 166927.0 | 24.574% | 1.899250 | 73.326% | 0.041088 | 0.624670 | 0.237069 | 0.717443 | 65.675% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

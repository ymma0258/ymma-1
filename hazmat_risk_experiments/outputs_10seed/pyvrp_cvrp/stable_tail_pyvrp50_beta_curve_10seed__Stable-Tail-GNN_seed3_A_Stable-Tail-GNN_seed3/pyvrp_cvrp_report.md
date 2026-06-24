# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 6.878324 | 0.000% | 0.198600 | 2.291333 | 0.216493 | 0.878165 | 89.534% |
| 0.25 | 0 | 141976.4 | 5.955% | 5.106014 | 25.767% | 0.149806 | 1.647166 | 0.219479 | 0.866939 | 87.600% |
| 0.5 | 0 | 147582.6 | 10.138% | 3.737482 | 45.663% | 0.108759 | 1.465473 | 0.310206 | 0.839522 | 83.702% |
| 1 | 0 | 154704.1 | 15.453% | 2.441121 | 64.510% | 0.058333 | 0.808732 | 0.239956 | 0.773618 | 74.814% |
| 2 | 0 | 166477.1 | 24.239% | 2.040797 | 70.330% | 0.043108 | 0.718972 | 0.268362 | 0.745340 | 70.462% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

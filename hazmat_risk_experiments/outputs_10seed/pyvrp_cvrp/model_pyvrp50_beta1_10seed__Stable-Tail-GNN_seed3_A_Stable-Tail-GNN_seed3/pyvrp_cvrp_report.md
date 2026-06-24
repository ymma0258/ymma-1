# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.695492 | 0.000% | 0.195570 | 2.189409 | 0.216915 | 0.875815 | 89.250% |
| 1 | 0 | 154704.1 | 15.453% | 2.441121 | 63.541% | 0.058333 | 0.808732 | 0.239956 | 0.773618 | 74.814% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

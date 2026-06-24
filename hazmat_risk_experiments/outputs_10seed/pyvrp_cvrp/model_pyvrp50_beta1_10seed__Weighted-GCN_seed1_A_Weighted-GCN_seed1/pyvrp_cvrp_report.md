# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.690716 | 0.000% | 0.248809 | 2.209356 | 0.147420 | 0.835843 | 86.383% |
| 1 | 0 | 157987.2 | 17.903% | 3.119899 | 59.433% | 0.063074 | 0.947181 | 0.229311 | 0.707205 | 70.275% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

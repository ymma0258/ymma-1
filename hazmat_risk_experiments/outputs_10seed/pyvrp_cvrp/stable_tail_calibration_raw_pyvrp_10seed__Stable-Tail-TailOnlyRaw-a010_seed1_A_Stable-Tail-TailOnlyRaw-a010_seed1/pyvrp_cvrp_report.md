# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.6 | 0.000% | 9.556943 | 0.000% | 0.306164 | 2.740793 | 0.168103 | 0.874546 | 89.903% |
| 0.25 | 0 | 141968.6 | 5.843% | 6.864558 | 28.172% | 0.213135 | 2.082295 | 0.203368 | 0.870950 | 88.660% |
| 0.5 | 0 | 147816.5 | 10.203% | 4.765552 | 50.135% | 0.119239 | 1.449409 | 0.201327 | 0.846821 | 84.424% |
| 1 | 0 | 156389.2 | 16.594% | 3.414474 | 64.272% | 0.078304 | 1.164702 | 0.255686 | 0.799368 | 77.876% |
| 2 | 0 | 168976.3 | 25.978% | 2.736249 | 71.369% | 0.056907 | 0.746404 | 0.185198 | 0.773898 | 73.722% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

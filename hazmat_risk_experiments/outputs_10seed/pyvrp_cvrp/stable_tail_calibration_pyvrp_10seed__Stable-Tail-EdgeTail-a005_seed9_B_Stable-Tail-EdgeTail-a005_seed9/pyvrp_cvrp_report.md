# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 8.639100 | 0.000% | 0.270614 | 2.850985 | 0.215301 | 0.869635 | 89.798% |
| 0.25 | 0 | 158607.0 | 7.800% | 7.704153 | 10.822% | 0.231076 | 2.591220 | 0.224828 | 0.868924 | 89.306% |
| 0.5 | 0 | 168609.2 | 14.598% | 5.374525 | 37.788% | 0.141626 | 1.891097 | 0.268076 | 0.848161 | 85.673% |
| 1 | 0 | 179839.6 | 22.231% | 3.388032 | 60.783% | 0.070584 | 1.083052 | 0.227287 | 0.805009 | 78.350% |
| 2 | 0 | 196935.2 | 33.851% | 2.988816 | 65.404% | 0.060021 | 0.952677 | 0.258643 | 0.790160 | 75.958% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

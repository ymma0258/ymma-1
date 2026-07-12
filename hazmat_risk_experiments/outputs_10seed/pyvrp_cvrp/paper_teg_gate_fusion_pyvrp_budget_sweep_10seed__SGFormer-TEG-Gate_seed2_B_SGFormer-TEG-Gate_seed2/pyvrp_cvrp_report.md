# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 9.354173 | 0.000% | 0.288063 | 3.403216 | 0.266114 | 0.876438 | 89.662% |
| 0.25 | 0 | 156979.8 | 6.839% | 7.698533 | 17.699% | 0.227234 | 2.753724 | 0.289721 | 0.871992 | 88.248% |
| 0.5 | 0 | 166112.9 | 13.055% | 6.721073 | 28.149% | 0.185993 | 2.333900 | 0.258703 | 0.869029 | 87.095% |
| 1 | 0 | 179204.0 | 21.965% | 4.219503 | 54.892% | 0.100544 | 1.597647 | 0.298993 | 0.833870 | 80.650% |
| 2 | 0 | 197208.6 | 34.219% | 3.582761 | 61.699% | 0.084393 | 1.689330 | 0.371475 | 0.817938 | 77.618% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

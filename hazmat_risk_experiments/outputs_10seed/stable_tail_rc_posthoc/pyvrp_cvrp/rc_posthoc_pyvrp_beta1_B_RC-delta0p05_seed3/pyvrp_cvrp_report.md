# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 6.983899 | 0.000% | 0.207273 | 2.399569 | 0.224795 | 0.872730 | 88.903% |
| 1 | 0 | 174071.4 | 18.633% | 2.900287 | 58.472% | 0.069727 | 1.103585 | 0.269605 | 0.795798 | 76.809% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

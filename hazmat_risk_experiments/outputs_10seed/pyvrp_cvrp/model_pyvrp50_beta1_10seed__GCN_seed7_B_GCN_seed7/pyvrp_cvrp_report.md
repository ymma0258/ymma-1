# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.442787 | 0.000% | 0.293933 | 3.399195 | 0.220726 | 0.856399 | 89.822% |
| 1 | 0 | 180891.4 | 23.281% | 5.343059 | 48.835% | 0.150212 | 1.700914 | 0.226783 | 0.819760 | 83.013% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

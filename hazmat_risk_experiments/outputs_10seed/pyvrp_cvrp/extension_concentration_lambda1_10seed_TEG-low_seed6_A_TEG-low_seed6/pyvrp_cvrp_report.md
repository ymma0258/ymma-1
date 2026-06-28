# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.216615 | 0.000% | 0.253968 | 2.469363 | 0.149142 | 0.847418 | 87.088% |
| 1 | 0 | 160133.0 | 19.504% | 3.251072 | 60.433% | 0.063925 | 1.004495 | 0.246543 | 0.739278 | 72.175% |
| 1 | 1 | 171795.0 | 28.208% | 2.672825 | 67.470% | 0.053286 | 0.949412 | 0.245279 | 0.692234 | 66.399% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

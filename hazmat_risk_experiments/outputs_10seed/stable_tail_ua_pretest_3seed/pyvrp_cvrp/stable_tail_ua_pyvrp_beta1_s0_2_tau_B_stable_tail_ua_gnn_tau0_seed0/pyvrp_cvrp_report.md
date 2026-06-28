# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 7.888864 | 0.000% | 0.232450 | 2.804705 | 0.244987 | 0.876005 | 89.991% |
| 1 | 0 | 177407.3 | 21.328% | 3.710084 | 52.971% | 0.093886 | 1.421461 | 0.336812 | 0.824516 | 81.282% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

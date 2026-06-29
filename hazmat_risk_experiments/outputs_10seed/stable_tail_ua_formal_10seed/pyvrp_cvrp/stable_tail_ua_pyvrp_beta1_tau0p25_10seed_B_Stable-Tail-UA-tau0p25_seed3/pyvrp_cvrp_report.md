# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 11.849915 | 0.000% | 0.302648 | 3.645547 | 0.184494 | 0.853949 | 88.811% |
| 1 | 0 | 180575.2 | 23.066% | 5.322208 | 55.087% | 0.106537 | 1.684203 | 0.224288 | 0.791196 | 79.492% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

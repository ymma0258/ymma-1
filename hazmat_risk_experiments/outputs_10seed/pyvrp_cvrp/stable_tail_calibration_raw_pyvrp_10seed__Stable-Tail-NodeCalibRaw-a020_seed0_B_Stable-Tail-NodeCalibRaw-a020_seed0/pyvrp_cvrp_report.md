# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.4 | 0.000% | 7.718027 | 0.000% | 0.218614 | 2.554412 | 0.240966 | 0.878031 | 89.520% |
| 0.25 | 0 | 157058.6 | 6.603% | 6.359706 | 17.599% | 0.159163 | 2.170854 | 0.237852 | 0.874343 | 88.366% |
| 0.5 | 0 | 165269.6 | 12.176% | 4.829663 | 37.424% | 0.123030 | 1.729439 | 0.257693 | 0.855079 | 85.158% |
| 1 | 0 | 175901.5 | 19.393% | 3.186160 | 58.718% | 0.076957 | 1.275565 | 0.306744 | 0.812387 | 78.418% |
| 2 | 0 | 191015.6 | 29.651% | 2.463173 | 68.085% | 0.052818 | 0.911027 | 0.286579 | 0.779327 | 72.499% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

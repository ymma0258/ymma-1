# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.7 | 0.000% | 6.058154 | 0.000% | 0.191584 | 2.039354 | 0.252618 | 0.876309 | 90.285% |
| 0.25 | 0 | 156022.7 | 6.044% | 4.991674 | 17.604% | 0.146007 | 1.739382 | 0.254321 | 0.873005 | 89.107% |
| 0.5 | 0 | 164025.1 | 11.483% | 4.064566 | 32.908% | 0.109431 | 1.312636 | 0.227146 | 0.860959 | 87.085% |
| 1 | 0 | 173605.8 | 17.994% | 2.398095 | 60.415% | 0.052853 | 0.874492 | 0.275245 | 0.818827 | 79.714% |
| 2 | 0 | 187309.1 | 27.308% | 1.934887 | 68.061% | 0.038954 | 0.711217 | 0.259538 | 0.792646 | 75.259% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

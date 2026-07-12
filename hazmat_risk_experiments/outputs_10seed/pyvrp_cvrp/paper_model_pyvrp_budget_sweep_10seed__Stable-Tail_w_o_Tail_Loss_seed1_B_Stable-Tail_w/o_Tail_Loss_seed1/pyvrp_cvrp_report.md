# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.2 | 0.000% | 8.426014 | 0.000% | 0.254360 | 2.850918 | 0.244705 | 0.881643 | 91.174% |
| 0.25 | 0 | 155955.3 | 5.950% | 6.836522 | 18.864% | 0.171235 | 2.130886 | 0.209969 | 0.881667 | 89.897% |
| 0.5 | 0 | 164110.1 | 11.490% | 5.713586 | 32.191% | 0.144393 | 1.827879 | 0.246513 | 0.873981 | 87.882% |
| 1 | 0 | 174385.5 | 18.471% | 3.688022 | 56.231% | 0.092288 | 1.319628 | 0.269047 | 0.849134 | 82.472% |
| 2 | 0 | 189716.7 | 28.886% | 2.817042 | 66.567% | 0.061883 | 1.062945 | 0.302869 | 0.827355 | 77.777% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

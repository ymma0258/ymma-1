# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 6.819767 | 0.000% | 0.179749 | 2.410616 | 0.257972 | 0.866248 | 88.725% |
| 0.25 | 0 | 156031.2 | 5.954% | 5.631657 | 17.422% | 0.140424 | 2.034754 | 0.273906 | 0.863424 | 87.619% |
| 0.5 | 0 | 163723.6 | 11.177% | 4.415128 | 35.260% | 0.112023 | 1.722406 | 0.274621 | 0.846536 | 84.736% |
| 1 | 0 | 175476.8 | 19.158% | 3.522100 | 48.355% | 0.094819 | 1.395660 | 0.309034 | 0.838689 | 82.288% |
| 2 | 0 | 193125.8 | 31.143% | 2.659006 | 61.010% | 0.064804 | 1.061468 | 0.284221 | 0.801089 | 76.339% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

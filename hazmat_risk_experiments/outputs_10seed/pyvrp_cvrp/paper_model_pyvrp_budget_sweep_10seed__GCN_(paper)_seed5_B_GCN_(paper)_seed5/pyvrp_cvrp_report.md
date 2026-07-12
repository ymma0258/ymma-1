# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.2 | 0.000% | 7.745751 | 0.000% | 0.216141 | 2.648196 | 0.238103 | 0.862497 | 88.659% |
| 0.25 | 0 | 156423.6 | 6.124% | 6.717324 | 13.277% | 0.163588 | 2.216712 | 0.210151 | 0.859680 | 88.278% |
| 0.5 | 0 | 165326.5 | 12.164% | 5.456162 | 29.559% | 0.135724 | 1.688618 | 0.175876 | 0.844417 | 85.933% |
| 1 | 0 | 177518.3 | 20.435% | 3.574736 | 53.849% | 0.092497 | 1.151969 | 0.258931 | 0.808301 | 80.102% |
| 2 | 0 | 193455.5 | 31.248% | 2.841546 | 63.315% | 0.066160 | 0.951586 | 0.269391 | 0.777099 | 75.093% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

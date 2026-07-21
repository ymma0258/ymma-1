# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 8.962315 | 0.000% | 0.278910 | 2.457036 | 0.148494 | 0.879852 | 90.382% |
| 0.25 | 0 | 142858.9 | 6.560% | 6.346998 | 29.181% | 0.204759 | 2.066685 | 0.252618 | 0.872458 | 88.560% |
| 0.5 | 0 | 149513.7 | 11.524% | 5.448272 | 39.209% | 0.169954 | 1.835166 | 0.255389 | 0.861106 | 86.792% |
| 1 | 0 | 158833.7 | 18.475% | 3.708732 | 58.619% | 0.101738 | 1.292615 | 0.304666 | 0.822469 | 80.954% |
| 2 | 0 | 173714.4 | 29.575% | 2.961279 | 66.959% | 0.067254 | 1.106245 | 0.332317 | 0.797981 | 76.887% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

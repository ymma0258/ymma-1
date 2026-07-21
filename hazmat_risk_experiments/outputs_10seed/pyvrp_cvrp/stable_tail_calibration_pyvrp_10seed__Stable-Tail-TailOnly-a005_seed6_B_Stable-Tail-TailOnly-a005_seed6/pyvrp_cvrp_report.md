# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.9 | 0.000% | 8.705795 | 0.000% | 0.250793 | 3.012822 | 0.240623 | 0.869694 | 89.362% |
| 0.25 | 0 | 158190.9 | 7.371% | 8.037332 | 7.678% | 0.205694 | 2.650970 | 0.235194 | 0.868715 | 89.236% |
| 0.5 | 0 | 168493.3 | 14.364% | 6.317211 | 27.437% | 0.162737 | 2.088742 | 0.244381 | 0.860176 | 87.016% |
| 1 | 0 | 181897.6 | 23.462% | 4.191227 | 51.857% | 0.105942 | 1.563637 | 0.324318 | 0.826215 | 81.047% |
| 2 | 0 | 202814.3 | 37.659% | 3.700128 | 57.498% | 0.092890 | 1.363948 | 0.331605 | 0.815833 | 79.048% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

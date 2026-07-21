# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.5 | 0.000% | 6.922211 | 0.000% | 0.198605 | 2.023268 | 0.167681 | 0.872533 | 89.058% |
| 0.25 | 0 | 141920.0 | 5.859% | 4.805267 | 30.582% | 0.139353 | 1.452658 | 0.198589 | 0.853283 | 86.458% |
| 0.5 | 0 | 147227.2 | 9.818% | 3.615631 | 47.768% | 0.107579 | 1.271022 | 0.244496 | 0.832025 | 82.891% |
| 1 | 0 | 155201.1 | 15.766% | 2.336127 | 66.252% | 0.058875 | 0.717675 | 0.234141 | 0.765311 | 73.441% |
| 2 | 0 | 167002.8 | 24.569% | 2.137855 | 69.116% | 0.052545 | 0.675539 | 0.258035 | 0.753150 | 71.736% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

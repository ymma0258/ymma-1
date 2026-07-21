# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.2 | 0.000% | 10.306033 | 0.000% | 0.326757 | 3.248413 | 0.203381 | 0.877412 | 91.131% |
| 0.25 | 0 | 158745.5 | 7.845% | 8.801471 | 14.599% | 0.247772 | 2.654010 | 0.211660 | 0.880018 | 90.860% |
| 0.5 | 0 | 168223.9 | 14.285% | 5.412182 | 47.485% | 0.149017 | 1.788229 | 0.272258 | 0.857812 | 86.243% |
| 1 | 0 | 179869.5 | 22.196% | 3.750451 | 63.609% | 0.081361 | 1.361753 | 0.305284 | 0.826796 | 80.989% |
| 2 | 0 | 197253.1 | 34.006% | 3.412846 | 66.885% | 0.067819 | 1.090535 | 0.248501 | 0.813021 | 78.780% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

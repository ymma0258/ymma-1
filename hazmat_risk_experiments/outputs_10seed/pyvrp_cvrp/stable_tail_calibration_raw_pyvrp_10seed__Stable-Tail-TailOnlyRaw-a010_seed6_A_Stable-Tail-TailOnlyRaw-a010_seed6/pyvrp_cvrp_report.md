# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 8.496933 | 0.000% | 0.256616 | 2.378768 | 0.164207 | 0.870786 | 89.373% |
| 0.25 | 0 | 143258.3 | 6.698% | 5.299262 | 37.633% | 0.155895 | 1.786088 | 0.257361 | 0.850506 | 85.903% |
| 0.5 | 0 | 149465.4 | 11.321% | 4.328965 | 49.053% | 0.131264 | 1.664846 | 0.310661 | 0.827837 | 83.036% |
| 1 | 0 | 158973.4 | 18.403% | 3.023712 | 64.414% | 0.081590 | 0.994397 | 0.265181 | 0.783777 | 76.601% |
| 2 | 0 | 173314.8 | 29.084% | 2.384841 | 71.933% | 0.056284 | 0.893184 | 0.321227 | 0.741736 | 70.700% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

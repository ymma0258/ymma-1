# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.9 | 0.000% | 8.615826 | 0.000% | 0.290835 | 2.483595 | 0.168589 | 0.876832 | 89.431% |
| 0.25 | 0 | 142157.6 | 5.774% | 5.378245 | 37.577% | 0.167330 | 1.554171 | 0.161650 | 0.866780 | 86.083% |
| 0.5 | 0 | 147446.4 | 9.709% | 4.035602 | 53.161% | 0.116644 | 1.677937 | 0.307984 | 0.841822 | 82.059% |
| 1 | 0 | 154928.6 | 15.276% | 2.462404 | 71.420% | 0.048731 | 0.763450 | 0.220728 | 0.780061 | 72.204% |
| 2 | 0 | 166423.8 | 23.829% | 2.216721 | 74.272% | 0.043805 | 0.725281 | 0.225232 | 0.765096 | 69.642% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

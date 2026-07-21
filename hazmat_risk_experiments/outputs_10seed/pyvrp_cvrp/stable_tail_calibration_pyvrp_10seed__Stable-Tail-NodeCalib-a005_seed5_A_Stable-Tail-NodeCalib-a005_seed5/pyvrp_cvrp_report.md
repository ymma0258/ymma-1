# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.7 | 0.000% | 7.223821 | 0.000% | 0.233195 | 2.132555 | 0.171986 | 0.870176 | 88.437% |
| 0.25 | 0 | 142826.9 | 6.219% | 4.788805 | 33.708% | 0.137356 | 1.526675 | 0.200982 | 0.849687 | 85.374% |
| 0.5 | 0 | 148340.8 | 10.320% | 3.751511 | 48.068% | 0.108896 | 1.381576 | 0.302424 | 0.827992 | 81.866% |
| 1 | 0 | 156488.6 | 16.379% | 2.563579 | 64.512% | 0.067071 | 1.015654 | 0.289704 | 0.777236 | 74.357% |
| 2 | 0 | 168744.0 | 25.493% | 1.885476 | 73.899% | 0.041175 | 0.601703 | 0.227157 | 0.716525 | 65.539% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

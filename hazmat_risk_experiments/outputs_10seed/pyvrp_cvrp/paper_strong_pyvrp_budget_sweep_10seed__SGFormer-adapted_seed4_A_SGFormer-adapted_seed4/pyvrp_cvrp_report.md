# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.9 | 0.000% | 9.863050 | 0.000% | 0.332777 | 3.032539 | 0.187435 | 0.888250 | 90.293% |
| 0.25 | 0 | 142782.1 | 6.238% | 6.167409 | 37.470% | 0.194321 | 2.149158 | 0.287855 | 0.872619 | 86.099% |
| 0.5 | 0 | 148728.2 | 10.663% | 4.908088 | 50.238% | 0.146086 | 1.629321 | 0.272891 | 0.849298 | 82.606% |
| 1 | 0 | 157111.7 | 16.900% | 3.546791 | 64.040% | 0.075714 | 1.294885 | 0.337513 | 0.807314 | 76.220% |
| 2 | 0 | 169728.6 | 26.288% | 2.810601 | 71.504% | 0.058023 | 1.295189 | 0.340057 | 0.774892 | 70.992% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

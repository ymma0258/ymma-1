# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 6.703398 | 0.000% | 0.206978 | 1.927776 | 0.165464 | 0.870898 | 88.587% |
| 0.25 | 0 | 142569.6 | 6.344% | 4.726927 | 29.485% | 0.133033 | 1.486045 | 0.213208 | 0.857243 | 86.036% |
| 0.5 | 0 | 148470.0 | 10.745% | 3.352541 | 49.987% | 0.097253 | 1.194508 | 0.266421 | 0.824422 | 81.145% |
| 1 | 0 | 156421.4 | 16.676% | 2.398848 | 64.214% | 0.062677 | 0.867631 | 0.256482 | 0.775015 | 74.133% |
| 2 | 0 | 167641.7 | 25.045% | 1.819379 | 72.859% | 0.039950 | 0.587728 | 0.223922 | 0.723897 | 66.566% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134265.0 | 0.000% | 9.036361 | 0.000% | 0.287154 | 2.755078 | 0.183943 | 0.878273 | 89.980% |
| 0.25 | 0 | 143406.0 | 6.808% | 6.528733 | 27.750% | 0.198615 | 2.069123 | 0.203569 | 0.871375 | 88.576% |
| 0.5 | 0 | 150299.4 | 11.942% | 4.956835 | 45.146% | 0.147069 | 1.653377 | 0.274338 | 0.854314 | 85.613% |
| 1 | 0 | 159695.5 | 18.941% | 3.672855 | 59.355% | 0.100420 | 1.239788 | 0.291126 | 0.821513 | 80.780% |
| 2 | 0 | 174966.5 | 30.314% | 2.907463 | 67.825% | 0.068338 | 1.083017 | 0.322032 | 0.793635 | 76.368% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

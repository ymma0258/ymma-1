# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.880606 | 0.000% | 0.259366 | 2.523894 | 0.141600 | 0.845007 | 87.680% |
| 1 | 0 | 161242.6 | 20.332% | 3.752201 | 57.748% | 0.099686 | 1.486296 | 0.311987 | 0.748959 | 74.355% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

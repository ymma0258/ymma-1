# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.6 | 0.000% | 7.882772 | 0.000% | 0.247299 | 2.394757 | 0.183015 | 0.870171 | 88.842% |
| 0.25 | 0 | 143204.3 | 6.764% | 4.677353 | 40.664% | 0.130525 | 1.514921 | 0.221873 | 0.846588 | 85.110% |
| 0.5 | 0 | 149717.5 | 11.620% | 4.007727 | 49.158% | 0.112348 | 1.426623 | 0.252411 | 0.825965 | 82.125% |
| 1 | 0 | 158776.2 | 18.373% | 2.769192 | 64.870% | 0.064596 | 0.874978 | 0.215260 | 0.780326 | 75.523% |
| 2 | 0 | 173885.0 | 29.638% | 2.244992 | 71.520% | 0.043515 | 0.688870 | 0.222959 | 0.743092 | 69.575% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 8.420553 | 0.000% | 0.270307 | 2.413201 | 0.162497 | 0.870835 | 89.569% |
| 0.25 | 0 | 142726.0 | 6.461% | 5.799191 | 31.131% | 0.161027 | 1.946618 | 0.235380 | 0.857755 | 87.453% |
| 0.5 | 0 | 148900.3 | 11.066% | 4.441525 | 47.254% | 0.110360 | 1.647545 | 0.245879 | 0.832708 | 84.028% |
| 1 | 0 | 157795.1 | 17.701% | 3.017247 | 64.168% | 0.069355 | 1.065030 | 0.254557 | 0.778387 | 76.492% |
| 2 | 0 | 171036.7 | 27.578% | 2.353515 | 72.050% | 0.052717 | 0.693055 | 0.225918 | 0.738470 | 70.572% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

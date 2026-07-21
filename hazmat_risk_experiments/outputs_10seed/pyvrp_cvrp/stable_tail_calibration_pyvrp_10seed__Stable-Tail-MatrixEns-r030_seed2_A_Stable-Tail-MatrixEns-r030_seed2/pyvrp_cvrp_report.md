# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 6.128172 | 0.000% | 0.198415 | 1.753753 | 0.165273 | 0.877768 | 89.990% |
| 0.25 | 0 | 142325.4 | 6.162% | 4.132355 | 32.568% | 0.123694 | 1.528042 | 0.309647 | 0.867150 | 87.834% |
| 0.5 | 0 | 148449.6 | 10.730% | 3.282446 | 46.437% | 0.098168 | 1.187561 | 0.262409 | 0.852834 | 85.211% |
| 1 | 0 | 157582.0 | 17.542% | 2.262207 | 63.085% | 0.061534 | 0.928001 | 0.341520 | 0.811319 | 78.987% |
| 2 | 0 | 171814.6 | 28.158% | 2.041944 | 66.679% | 0.051443 | 0.842150 | 0.341571 | 0.797759 | 76.723% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 7.580441 | 0.000% | 0.233208 | 2.188264 | 0.169093 | 0.876752 | 89.362% |
| 0.25 | 0 | 142420.1 | 6.232% | 5.380864 | 29.016% | 0.152892 | 1.700330 | 0.231190 | 0.864792 | 87.059% |
| 0.5 | 0 | 148009.0 | 10.401% | 3.641116 | 51.967% | 0.107508 | 1.496607 | 0.338556 | 0.827350 | 81.623% |
| 1 | 0 | 155604.4 | 16.067% | 2.428522 | 67.963% | 0.062781 | 0.996674 | 0.307524 | 0.767783 | 72.874% |
| 2 | 0 | 166839.9 | 24.447% | 1.865071 | 75.396% | 0.040321 | 0.623727 | 0.228810 | 0.713613 | 65.349% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

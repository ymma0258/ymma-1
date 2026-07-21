# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 9.224787 | 0.000% | 0.291342 | 3.195657 | 0.252714 | 0.872708 | 89.830% |
| 0.25 | 0 | 155773.1 | 6.018% | 7.635964 | 17.223% | 0.210387 | 2.644256 | 0.250490 | 0.868235 | 88.641% |
| 0.5 | 0 | 164003.5 | 11.620% | 6.406483 | 30.551% | 0.159750 | 1.895733 | 0.183684 | 0.860346 | 86.984% |
| 1 | 0 | 173737.9 | 18.245% | 3.740242 | 59.454% | 0.089392 | 1.394145 | 0.278714 | 0.814611 | 79.167% |
| 2 | 0 | 187513.7 | 27.621% | 2.988758 | 67.601% | 0.058764 | 1.098084 | 0.265660 | 0.790861 | 75.025% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

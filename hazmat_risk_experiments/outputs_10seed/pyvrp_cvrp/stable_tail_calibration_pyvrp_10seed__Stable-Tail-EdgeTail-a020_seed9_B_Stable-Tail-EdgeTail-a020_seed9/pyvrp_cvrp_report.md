# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 9.212009 | 0.000% | 0.291706 | 2.937338 | 0.214610 | 0.872608 | 90.151% |
| 0.25 | 0 | 157795.7 | 7.443% | 7.903852 | 14.201% | 0.224026 | 2.679269 | 0.248958 | 0.872040 | 89.823% |
| 0.5 | 0 | 167555.3 | 14.089% | 5.397277 | 41.410% | 0.146679 | 1.868113 | 0.287503 | 0.850486 | 85.729% |
| 1 | 0 | 178716.8 | 21.689% | 3.655173 | 60.322% | 0.079692 | 1.221890 | 0.246868 | 0.817102 | 80.082% |
| 2 | 0 | 195511.7 | 33.124% | 3.028611 | 67.123% | 0.058749 | 0.983947 | 0.258118 | 0.792475 | 76.300% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

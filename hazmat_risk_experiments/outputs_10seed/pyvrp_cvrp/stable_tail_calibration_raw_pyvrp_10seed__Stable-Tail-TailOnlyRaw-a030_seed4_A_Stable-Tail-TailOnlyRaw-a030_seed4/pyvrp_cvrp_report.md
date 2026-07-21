# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.1 | 0.000% | 9.939112 | 0.000% | 0.307879 | 2.857787 | 0.158457 | 0.886962 | 91.276% |
| 0.25 | 0 | 143173.8 | 6.688% | 7.519048 | 24.349% | 0.240772 | 2.344612 | 0.253098 | 0.884297 | 90.140% |
| 0.5 | 0 | 150218.9 | 11.938% | 5.672600 | 42.926% | 0.177320 | 2.016147 | 0.273755 | 0.867633 | 87.515% |
| 1 | 0 | 160020.1 | 19.242% | 4.261112 | 57.128% | 0.119604 | 1.429989 | 0.285528 | 0.840952 | 83.327% |
| 2 | 0 | 174899.7 | 30.329% | 3.318986 | 66.607% | 0.084858 | 1.262295 | 0.360636 | 0.815895 | 79.172% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

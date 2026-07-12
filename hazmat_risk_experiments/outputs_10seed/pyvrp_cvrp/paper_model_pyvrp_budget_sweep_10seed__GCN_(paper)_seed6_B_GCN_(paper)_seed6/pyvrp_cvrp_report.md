# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.6 | 0.000% | 9.253855 | 0.000% | 0.281370 | 3.153452 | 0.229543 | 0.847387 | 88.806% |
| 0.25 | 0 | 158683.7 | 7.803% | 8.185313 | 11.547% | 0.198438 | 2.641796 | 0.215721 | 0.848771 | 88.790% |
| 0.5 | 0 | 169869.0 | 15.402% | 6.589076 | 28.796% | 0.167206 | 1.994784 | 0.205418 | 0.834748 | 86.275% |
| 1 | 0 | 185160.7 | 25.791% | 5.076996 | 45.136% | 0.126740 | 1.712216 | 0.270135 | 0.812534 | 82.538% |
| 2 | 0 | 209457.8 | 42.297% | 3.987131 | 56.914% | 0.091302 | 1.439430 | 0.320239 | 0.781301 | 77.655% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

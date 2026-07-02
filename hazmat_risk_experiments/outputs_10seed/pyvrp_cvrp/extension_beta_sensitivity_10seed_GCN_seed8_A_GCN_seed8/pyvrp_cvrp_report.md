# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.925623 | 0.000% | 0.246790 | 2.316011 | 0.150048 | 0.872615 | 89.748% |
| 0.5 | 0 | 150393.0 | 12.236% | 4.588144 | 42.110% | 0.108466 | 1.700997 | 0.274897 | 0.843621 | 85.013% |
| 1 | 0 | 160243.5 | 19.587% | 3.300414 | 58.358% | 0.075381 | 1.172542 | 0.302583 | 0.809202 | 79.525% |
| 1.5 | 0 | 168774.5 | 25.953% | 2.837525 | 64.198% | 0.058542 | 1.014364 | 0.306716 | 0.790543 | 76.544% |
| 2 | 0 | 176119.9 | 31.435% | 2.763928 | 65.127% | 0.055669 | 1.005731 | 0.302787 | 0.782333 | 75.433% |
| 3 | 0 | 188302.2 | 40.527% | 2.351703 | 70.328% | 0.049328 | 1.009015 | 0.344686 | 0.751646 | 70.876% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

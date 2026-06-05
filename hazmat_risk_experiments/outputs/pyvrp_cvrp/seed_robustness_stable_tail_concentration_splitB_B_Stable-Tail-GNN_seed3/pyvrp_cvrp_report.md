# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 6.678740 | 0.000% | 0.183932 | 2.449276 | 0.248736 | 0.873500 | 88.871% |
| 1 | 0 | 174010.4 | 18.753% | 3.048816 | 54.350% | 0.077177 | 1.201823 | 0.294764 | 0.808027 | 78.681% |
| 1 | 1 | 185996.0 | 26.933% | 2.289109 | 65.725% | 0.045568 | 0.849260 | 0.276995 | 0.769283 | 72.320% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

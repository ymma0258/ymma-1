# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 8.220912 | 0.000% | 0.253618 | 2.423365 | 0.180885 | 0.882725 | 90.424% |
| 0.25 | 0 | 143387.4 | 7.007% | 5.430847 | 33.939% | 0.172401 | 1.748625 | 0.209272 | 0.871199 | 88.115% |
| 0.5 | 0 | 149803.0 | 11.795% | 3.937004 | 52.110% | 0.102053 | 1.499626 | 0.277444 | 0.839354 | 83.782% |
| 1 | 0 | 158825.7 | 18.528% | 2.736290 | 66.715% | 0.061359 | 0.939604 | 0.263897 | 0.802747 | 77.160% |
| 2 | 0 | 172080.7 | 28.420% | 1.798155 | 78.127% | 0.035444 | 0.557767 | 0.245135 | 0.727299 | 66.270% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

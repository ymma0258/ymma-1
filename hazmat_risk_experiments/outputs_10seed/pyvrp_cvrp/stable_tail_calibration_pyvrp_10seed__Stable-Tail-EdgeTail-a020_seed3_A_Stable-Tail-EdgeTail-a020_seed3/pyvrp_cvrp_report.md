# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 6.802915 | 0.000% | 0.197173 | 2.055199 | 0.177048 | 0.871817 | 88.838% |
| 0.25 | 0 | 141573.5 | 5.601% | 4.814709 | 29.226% | 0.136566 | 1.494293 | 0.209920 | 0.857178 | 86.716% |
| 0.5 | 0 | 147039.1 | 9.678% | 3.801458 | 44.120% | 0.106437 | 1.315678 | 0.231595 | 0.837146 | 83.657% |
| 1 | 0 | 154473.1 | 15.223% | 2.383203 | 64.968% | 0.061310 | 0.736587 | 0.228850 | 0.769890 | 74.394% |
| 2 | 0 | 165991.2 | 23.814% | 2.181173 | 67.938% | 0.053147 | 0.698544 | 0.217696 | 0.754588 | 71.980% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

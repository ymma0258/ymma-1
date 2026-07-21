# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.2 | 0.000% | 7.391655 | 0.000% | 0.227324 | 2.166653 | 0.175782 | 0.869090 | 88.582% |
| 0.25 | 0 | 143254.7 | 6.908% | 5.316814 | 28.070% | 0.150520 | 1.727661 | 0.231921 | 0.859473 | 87.154% |
| 0.5 | 0 | 149500.6 | 11.569% | 3.930131 | 46.830% | 0.114511 | 1.569709 | 0.276409 | 0.834655 | 83.475% |
| 1 | 0 | 158482.2 | 18.272% | 2.713452 | 63.290% | 0.068500 | 0.828944 | 0.221423 | 0.784123 | 76.117% |
| 2 | 0 | 173433.9 | 29.430% | 2.242834 | 69.657% | 0.046218 | 0.659070 | 0.212540 | 0.755902 | 71.393% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

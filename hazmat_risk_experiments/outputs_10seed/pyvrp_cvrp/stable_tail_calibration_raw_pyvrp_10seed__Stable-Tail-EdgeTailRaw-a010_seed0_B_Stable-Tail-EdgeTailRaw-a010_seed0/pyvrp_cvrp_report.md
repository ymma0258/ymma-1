# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.9 | 0.000% | 7.847392 | 0.000% | 0.223481 | 2.630833 | 0.256903 | 0.879817 | 89.839% |
| 0.25 | 0 | 156684.1 | 6.397% | 6.448712 | 17.823% | 0.157408 | 2.395842 | 0.277465 | 0.872982 | 88.525% |
| 0.5 | 0 | 164837.7 | 11.934% | 4.497299 | 42.691% | 0.114289 | 1.547772 | 0.243514 | 0.849771 | 84.343% |
| 1 | 0 | 175824.3 | 19.394% | 3.079035 | 60.764% | 0.078015 | 1.157989 | 0.281975 | 0.810284 | 78.101% |
| 2 | 0 | 190643.2 | 29.457% | 2.379778 | 69.674% | 0.049305 | 0.929765 | 0.274333 | 0.777342 | 72.179% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.6 | 0.000% | 8.904758 | 0.000% | 0.280457 | 2.550947 | 0.171069 | 0.879275 | 90.134% |
| 0.25 | 0 | 143265.7 | 6.810% | 6.991128 | 21.490% | 0.216607 | 2.100583 | 0.215085 | 0.875954 | 89.335% |
| 0.5 | 0 | 150091.9 | 11.899% | 4.890713 | 45.078% | 0.147523 | 1.806839 | 0.310155 | 0.848635 | 85.224% |
| 1 | 0 | 159802.3 | 19.138% | 3.659917 | 58.899% | 0.098414 | 1.332627 | 0.318421 | 0.820033 | 80.700% |
| 2 | 0 | 174985.3 | 30.458% | 2.773062 | 68.859% | 0.062550 | 1.052999 | 0.343091 | 0.783390 | 75.036% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

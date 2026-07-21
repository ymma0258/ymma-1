# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 9.009257 | 0.000% | 0.290875 | 2.412746 | 0.138327 | 0.872147 | 89.672% |
| 0.25 | 0 | 141853.9 | 5.810% | 6.211759 | 31.051% | 0.195739 | 1.877885 | 0.202639 | 0.864988 | 87.575% |
| 0.5 | 0 | 147630.9 | 10.119% | 4.658529 | 48.292% | 0.130048 | 1.508727 | 0.191852 | 0.840642 | 83.841% |
| 1 | 0 | 156059.4 | 16.406% | 3.190162 | 64.590% | 0.071457 | 1.083735 | 0.244437 | 0.790681 | 76.454% |
| 2 | 0 | 168432.7 | 25.635% | 2.634422 | 70.759% | 0.052816 | 0.783474 | 0.241801 | 0.767983 | 72.786% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.711599 | 0.000% | 0.212640 | 2.430709 | 0.179976 | 0.838649 | 86.539% |
| 1 | 0 | 158701.8 | 18.436% | 2.966485 | 61.532% | 0.063147 | 0.959999 | 0.217859 | 0.699891 | 68.916% |
| 1 | 1 | 168452.7 | 25.713% | 2.341437 | 69.637% | 0.040526 | 0.618936 | 0.129541 | 0.622710 | 59.904% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

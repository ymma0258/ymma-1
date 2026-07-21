# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 8.176866 | 0.000% | 0.250569 | 2.351872 | 0.154720 | 0.865227 | 88.484% |
| 0.25 | 0 | 143229.6 | 6.624% | 5.156610 | 36.937% | 0.144512 | 1.531927 | 0.196921 | 0.846022 | 85.460% |
| 0.5 | 0 | 149341.7 | 11.174% | 3.945914 | 51.743% | 0.114634 | 1.368950 | 0.270951 | 0.818300 | 81.550% |
| 1 | 0 | 158308.0 | 17.849% | 2.918817 | 64.304% | 0.078286 | 0.927610 | 0.251878 | 0.776559 | 75.676% |
| 2 | 0 | 172667.5 | 28.538% | 2.370401 | 71.011% | 0.055843 | 0.834059 | 0.269578 | 0.738357 | 70.346% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

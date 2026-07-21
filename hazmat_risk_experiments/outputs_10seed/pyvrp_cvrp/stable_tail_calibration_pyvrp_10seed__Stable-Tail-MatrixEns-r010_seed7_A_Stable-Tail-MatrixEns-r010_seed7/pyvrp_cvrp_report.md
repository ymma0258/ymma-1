# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 8.101063 | 0.000% | 0.266842 | 2.325783 | 0.168009 | 0.873128 | 89.495% |
| 0.25 | 0 | 142996.4 | 6.715% | 5.399167 | 33.352% | 0.160210 | 1.724085 | 0.204928 | 0.860256 | 86.831% |
| 0.5 | 0 | 149225.9 | 11.364% | 4.202920 | 48.119% | 0.124507 | 1.472144 | 0.240855 | 0.839914 | 83.787% |
| 1 | 0 | 158438.5 | 18.239% | 2.948908 | 63.599% | 0.080409 | 1.033563 | 0.254019 | 0.799687 | 77.376% |
| 2 | 0 | 171202.2 | 27.765% | 2.320610 | 71.354% | 0.055298 | 0.766687 | 0.270322 | 0.762967 | 71.547% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

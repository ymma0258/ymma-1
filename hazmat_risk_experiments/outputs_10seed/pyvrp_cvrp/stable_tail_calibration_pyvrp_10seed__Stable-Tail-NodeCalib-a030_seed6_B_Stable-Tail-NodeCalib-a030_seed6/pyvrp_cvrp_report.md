# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 8.986270 | 0.000% | 0.249265 | 2.969299 | 0.220957 | 0.869779 | 89.194% |
| 0.25 | 0 | 157724.6 | 7.346% | 7.740290 | 13.865% | 0.193418 | 2.580669 | 0.240725 | 0.868332 | 89.124% |
| 0.5 | 0 | 167931.6 | 14.293% | 6.263564 | 30.299% | 0.161904 | 2.224446 | 0.257273 | 0.857213 | 86.701% |
| 1 | 0 | 181306.7 | 23.396% | 4.238959 | 52.828% | 0.110601 | 1.577271 | 0.308853 | 0.827587 | 81.362% |
| 2 | 0 | 202025.4 | 37.497% | 3.721945 | 58.582% | 0.094625 | 1.421986 | 0.351467 | 0.818009 | 79.326% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

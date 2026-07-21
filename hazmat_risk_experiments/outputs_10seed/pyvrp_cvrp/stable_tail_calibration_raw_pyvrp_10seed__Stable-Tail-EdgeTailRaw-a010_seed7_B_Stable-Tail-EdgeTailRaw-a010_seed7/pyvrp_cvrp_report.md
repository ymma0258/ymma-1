# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.8 | 0.000% | 10.154815 | 0.000% | 0.304899 | 3.083904 | 0.193059 | 0.880509 | 90.740% |
| 0.25 | 0 | 157802.7 | 7.399% | 8.265601 | 18.604% | 0.240796 | 2.586728 | 0.210886 | 0.878232 | 89.716% |
| 0.5 | 0 | 167337.9 | 13.889% | 6.021495 | 40.703% | 0.167729 | 2.252393 | 0.306979 | 0.861371 | 86.200% |
| 1 | 0 | 178547.5 | 21.518% | 3.834193 | 62.243% | 0.094901 | 1.252957 | 0.211770 | 0.821687 | 79.368% |
| 2 | 0 | 195409.7 | 32.994% | 3.454013 | 65.986% | 0.079847 | 1.098674 | 0.232897 | 0.812578 | 77.682% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

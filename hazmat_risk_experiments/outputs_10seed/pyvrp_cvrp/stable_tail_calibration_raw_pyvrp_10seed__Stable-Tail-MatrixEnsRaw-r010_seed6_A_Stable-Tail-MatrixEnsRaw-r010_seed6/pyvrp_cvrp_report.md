# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.4 | 0.000% | 7.095159 | 0.000% | 0.204645 | 2.008125 | 0.153963 | 0.866122 | 88.526% |
| 0.25 | 0 | 143276.0 | 6.818% | 4.540821 | 36.001% | 0.129844 | 1.534103 | 0.275585 | 0.847968 | 85.396% |
| 0.5 | 0 | 149300.5 | 11.309% | 3.683185 | 48.089% | 0.109283 | 1.463124 | 0.324383 | 0.821236 | 82.148% |
| 1 | 0 | 159023.2 | 18.558% | 2.535491 | 64.264% | 0.066647 | 0.777448 | 0.254231 | 0.774173 | 75.271% |
| 2 | 0 | 173226.3 | 29.147% | 2.083595 | 70.634% | 0.048813 | 0.781982 | 0.304650 | 0.733649 | 69.692% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

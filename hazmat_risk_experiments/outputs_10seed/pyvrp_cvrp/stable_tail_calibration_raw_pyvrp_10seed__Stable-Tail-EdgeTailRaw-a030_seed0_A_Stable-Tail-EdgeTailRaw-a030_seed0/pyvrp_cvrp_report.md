# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.9 | 0.000% | 8.101484 | 0.000% | 0.248316 | 2.436764 | 0.202961 | 0.887134 | 90.788% |
| 0.25 | 0 | 142025.9 | 5.676% | 4.840161 | 40.256% | 0.143384 | 1.506576 | 0.215218 | 0.863902 | 86.743% |
| 0.5 | 0 | 147428.6 | 9.696% | 3.876888 | 52.146% | 0.115630 | 1.614470 | 0.316624 | 0.845378 | 84.245% |
| 1 | 0 | 155067.2 | 15.379% | 2.436871 | 69.921% | 0.056965 | 0.993556 | 0.297811 | 0.782812 | 74.898% |
| 2 | 0 | 166625.4 | 23.979% | 1.811789 | 77.636% | 0.033696 | 0.550144 | 0.204756 | 0.728596 | 66.499% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

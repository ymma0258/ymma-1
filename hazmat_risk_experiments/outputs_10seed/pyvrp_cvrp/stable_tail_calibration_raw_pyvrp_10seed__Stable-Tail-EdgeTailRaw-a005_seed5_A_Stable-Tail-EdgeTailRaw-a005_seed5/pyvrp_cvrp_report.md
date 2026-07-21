# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.7 | 0.000% | 7.681389 | 0.000% | 0.239599 | 2.147898 | 0.159653 | 0.873641 | 89.043% |
| 0.25 | 0 | 142382.3 | 6.046% | 5.102872 | 33.568% | 0.143931 | 1.669814 | 0.231600 | 0.859259 | 86.354% |
| 0.5 | 0 | 148178.0 | 10.363% | 3.498606 | 54.453% | 0.100141 | 1.210972 | 0.279775 | 0.819897 | 80.583% |
| 1 | 0 | 156109.8 | 16.270% | 2.634295 | 65.705% | 0.068666 | 0.998117 | 0.247141 | 0.778738 | 74.542% |
| 2 | 0 | 167335.6 | 24.631% | 1.903563 | 75.219% | 0.041420 | 0.605504 | 0.231790 | 0.717300 | 65.813% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

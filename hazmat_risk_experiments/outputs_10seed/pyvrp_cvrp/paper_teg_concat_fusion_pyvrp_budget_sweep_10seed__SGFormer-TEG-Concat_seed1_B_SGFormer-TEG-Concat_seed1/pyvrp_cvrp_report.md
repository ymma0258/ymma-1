# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.1 | 0.000% | 8.616273 | 0.000% | 0.262145 | 2.796031 | 0.241732 | 0.876883 | 88.974% |
| 0.25 | 0 | 157212.1 | 6.707% | 6.819101 | 20.858% | 0.205006 | 2.124898 | 0.206094 | 0.870166 | 87.225% |
| 0.5 | 0 | 165974.1 | 12.655% | 5.690728 | 33.954% | 0.166910 | 1.879089 | 0.222383 | 0.860770 | 85.291% |
| 1 | 0 | 177419.8 | 20.423% | 3.762743 | 56.330% | 0.093583 | 1.165284 | 0.222916 | 0.827250 | 79.143% |
| 2 | 0 | 194909.2 | 32.294% | 3.159856 | 63.327% | 0.069918 | 1.080460 | 0.286372 | 0.816465 | 76.584% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

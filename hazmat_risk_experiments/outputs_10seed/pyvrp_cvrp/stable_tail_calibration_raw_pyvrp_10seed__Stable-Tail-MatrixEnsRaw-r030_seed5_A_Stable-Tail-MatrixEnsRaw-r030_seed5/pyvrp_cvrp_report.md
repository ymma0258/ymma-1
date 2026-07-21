# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.4 | 0.000% | 5.301137 | 0.000% | 0.162676 | 1.596129 | 0.193319 | 0.876777 | 89.316% |
| 0.25 | 0 | 142507.5 | 6.350% | 3.701934 | 30.167% | 0.105844 | 1.397169 | 0.288064 | 0.862682 | 86.774% |
| 0.5 | 0 | 147930.4 | 10.397% | 2.567314 | 51.570% | 0.075048 | 0.959838 | 0.312026 | 0.829411 | 81.898% |
| 1 | 0 | 155945.0 | 16.378% | 1.773673 | 66.542% | 0.046177 | 0.685413 | 0.292841 | 0.775671 | 74.027% |
| 2 | 0 | 167061.9 | 24.675% | 1.325852 | 74.989% | 0.028740 | 0.432910 | 0.255585 | 0.718329 | 65.699% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

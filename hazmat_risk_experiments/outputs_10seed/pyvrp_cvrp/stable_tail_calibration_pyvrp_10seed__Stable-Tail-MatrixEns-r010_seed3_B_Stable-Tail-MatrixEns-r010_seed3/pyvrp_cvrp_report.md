# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 6.299591 | 0.000% | 0.196641 | 2.139287 | 0.240888 | 0.868793 | 88.920% |
| 0.25 | 0 | 155239.1 | 5.703% | 5.170628 | 17.921% | 0.127582 | 1.853293 | 0.268126 | 0.863299 | 87.822% |
| 0.5 | 0 | 162911.2 | 10.927% | 4.064691 | 35.477% | 0.103028 | 1.439574 | 0.246028 | 0.849944 | 85.220% |
| 1 | 0 | 174878.6 | 19.075% | 3.258340 | 48.277% | 0.083753 | 1.207838 | 0.273003 | 0.839336 | 82.650% |
| 2 | 0 | 192271.6 | 30.918% | 2.396245 | 61.962% | 0.058822 | 1.023155 | 0.310519 | 0.804735 | 76.822% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

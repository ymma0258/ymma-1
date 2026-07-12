# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147463.6 | 0.000% | 8.051766 | 0.000% | 0.253507 | 2.383793 | 0.204229 | 0.879382 | 88.311% |
| 0.25 | 0 | 156501.0 | 6.129% | 6.668845 | 17.175% | 0.198383 | 2.138889 | 0.206914 | 0.869797 | 86.655% |
| 0.5 | 0 | 163198.0 | 10.670% | 4.297104 | 46.632% | 0.100760 | 1.351641 | 0.239046 | 0.828254 | 79.810% |
| 1 | 0 | 171714.3 | 16.445% | 3.105118 | 61.436% | 0.054171 | 0.927264 | 0.210344 | 0.791184 | 73.847% |
| 2 | 0 | 185472.9 | 25.775% | 2.545972 | 68.380% | 0.040457 | 0.819771 | 0.221691 | 0.765876 | 69.319% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

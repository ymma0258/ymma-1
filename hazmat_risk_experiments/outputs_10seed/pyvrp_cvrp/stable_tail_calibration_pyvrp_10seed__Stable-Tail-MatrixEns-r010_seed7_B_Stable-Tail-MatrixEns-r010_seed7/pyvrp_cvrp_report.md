# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 9.065814 | 0.000% | 0.273636 | 2.737173 | 0.180743 | 0.877763 | 90.570% |
| 0.25 | 0 | 157532.4 | 7.264% | 7.384900 | 18.541% | 0.217547 | 2.396947 | 0.215024 | 0.876738 | 89.670% |
| 0.5 | 0 | 167058.8 | 13.751% | 5.393379 | 40.509% | 0.151891 | 1.840425 | 0.248277 | 0.858025 | 85.886% |
| 1 | 0 | 178418.7 | 21.486% | 3.553449 | 60.804% | 0.086743 | 1.194873 | 0.240026 | 0.826799 | 80.192% |
| 2 | 0 | 195191.6 | 32.906% | 2.959285 | 67.358% | 0.062400 | 0.947646 | 0.226442 | 0.807474 | 76.905% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

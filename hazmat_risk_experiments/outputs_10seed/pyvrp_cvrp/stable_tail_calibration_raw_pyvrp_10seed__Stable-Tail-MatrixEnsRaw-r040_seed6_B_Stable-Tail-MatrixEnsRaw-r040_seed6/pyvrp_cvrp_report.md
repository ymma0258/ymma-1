# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.1 | 0.000% | 5.398458 | 0.000% | 0.164157 | 1.800422 | 0.217714 | 0.870466 | 89.262% |
| 0.25 | 0 | 157661.9 | 7.109% | 4.838293 | 10.376% | 0.123580 | 1.654004 | 0.240549 | 0.871696 | 89.520% |
| 0.5 | 0 | 168185.0 | 14.258% | 3.737050 | 30.776% | 0.095240 | 1.271660 | 0.251557 | 0.858204 | 86.818% |
| 1 | 0 | 180903.1 | 22.899% | 2.562444 | 52.534% | 0.065418 | 0.960040 | 0.326278 | 0.830365 | 81.622% |
| 2 | 0 | 201797.1 | 37.093% | 2.330457 | 56.831% | 0.060010 | 0.842995 | 0.323054 | 0.822025 | 79.968% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

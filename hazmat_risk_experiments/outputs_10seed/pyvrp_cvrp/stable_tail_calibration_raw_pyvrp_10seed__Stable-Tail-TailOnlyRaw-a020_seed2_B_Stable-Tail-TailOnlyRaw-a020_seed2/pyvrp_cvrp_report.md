# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.7 | 0.000% | 9.897566 | 0.000% | 0.315398 | 3.820824 | 0.330112 | 0.882391 | 90.797% |
| 0.25 | 0 | 157259.2 | 6.739% | 8.316162 | 15.978% | 0.255146 | 3.264788 | 0.302870 | 0.878672 | 89.878% |
| 0.5 | 0 | 165362.9 | 12.239% | 6.608170 | 33.234% | 0.179490 | 2.589960 | 0.300829 | 0.868763 | 87.846% |
| 1 | 0 | 177888.7 | 20.741% | 4.766305 | 51.844% | 0.124803 | 1.904554 | 0.314803 | 0.850122 | 84.073% |
| 2 | 0 | 196408.4 | 33.311% | 3.933114 | 60.262% | 0.101033 | 1.949472 | 0.397519 | 0.838126 | 81.478% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

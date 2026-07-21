# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147396.9 | 0.000% | 8.642316 | 0.000% | 0.270250 | 3.433246 | 0.321856 | 0.872183 | 89.183% |
| 0.25 | 0 | 156859.7 | 6.420% | 7.746962 | 10.360% | 0.235618 | 3.107223 | 0.322655 | 0.873020 | 89.205% |
| 0.5 | 0 | 165587.1 | 12.341% | 5.873502 | 32.038% | 0.159043 | 2.098469 | 0.239194 | 0.859080 | 86.442% |
| 1 | 0 | 178918.2 | 21.385% | 4.414559 | 48.919% | 0.113872 | 1.575625 | 0.271703 | 0.840905 | 82.871% |
| 2 | 0 | 197506.7 | 33.997% | 3.614615 | 58.175% | 0.090785 | 1.682677 | 0.375192 | 0.824846 | 79.774% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

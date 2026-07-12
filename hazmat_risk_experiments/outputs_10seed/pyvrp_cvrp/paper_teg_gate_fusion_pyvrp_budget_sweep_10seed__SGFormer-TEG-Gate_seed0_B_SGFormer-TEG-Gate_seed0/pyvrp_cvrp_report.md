# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 8.204520 | 0.000% | 0.246984 | 2.509166 | 0.189790 | 0.867386 | 87.635% |
| 0.25 | 0 | 157212.3 | 6.998% | 6.970308 | 15.043% | 0.211922 | 2.269970 | 0.238764 | 0.864209 | 87.003% |
| 0.5 | 0 | 165483.4 | 12.627% | 4.325793 | 47.275% | 0.110793 | 1.368977 | 0.223566 | 0.815176 | 79.908% |
| 1 | 0 | 174725.2 | 18.917% | 2.957873 | 63.948% | 0.065806 | 1.010259 | 0.220811 | 0.764269 | 71.983% |
| 2 | 0 | 190417.7 | 29.597% | 2.724336 | 66.795% | 0.059721 | 0.898889 | 0.244193 | 0.750697 | 70.004% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

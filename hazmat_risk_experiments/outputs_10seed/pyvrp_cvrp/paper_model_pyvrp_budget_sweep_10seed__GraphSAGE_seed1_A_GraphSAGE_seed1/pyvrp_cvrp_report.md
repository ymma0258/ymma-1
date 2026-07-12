# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.2 | 0.000% | 7.956225 | 0.000% | 0.253694 | 2.533779 | 0.200382 | 0.884015 | 89.708% |
| 0.25 | 0 | 142227.7 | 5.878% | 5.179756 | 34.897% | 0.151479 | 1.605396 | 0.196427 | 0.870367 | 87.122% |
| 0.5 | 0 | 147746.3 | 9.987% | 3.728726 | 53.134% | 0.108500 | 1.485258 | 0.291378 | 0.844815 | 83.075% |
| 1 | 0 | 155125.2 | 15.480% | 2.382474 | 70.055% | 0.053976 | 0.752956 | 0.189413 | 0.781666 | 73.810% |
| 2 | 0 | 166870.6 | 24.223% | 1.967209 | 75.275% | 0.040574 | 0.626515 | 0.220620 | 0.757548 | 69.446% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

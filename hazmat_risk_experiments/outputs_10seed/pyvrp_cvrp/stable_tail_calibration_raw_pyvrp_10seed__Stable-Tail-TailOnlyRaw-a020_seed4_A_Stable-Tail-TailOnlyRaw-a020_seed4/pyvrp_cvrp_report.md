# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.5 | 0.000% | 9.660854 | 0.000% | 0.309973 | 2.941709 | 0.184535 | 0.883264 | 90.733% |
| 0.25 | 0 | 143572.2 | 6.879% | 7.399896 | 23.403% | 0.228888 | 2.206873 | 0.211098 | 0.881880 | 90.075% |
| 0.5 | 0 | 150353.7 | 11.927% | 5.323898 | 44.892% | 0.164592 | 1.603302 | 0.222738 | 0.861487 | 86.573% |
| 1 | 0 | 160241.7 | 19.288% | 4.037711 | 58.205% | 0.114466 | 1.476952 | 0.327844 | 0.836223 | 82.674% |
| 2 | 0 | 175016.0 | 30.287% | 3.168276 | 67.205% | 0.075973 | 1.181078 | 0.322941 | 0.806121 | 77.956% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

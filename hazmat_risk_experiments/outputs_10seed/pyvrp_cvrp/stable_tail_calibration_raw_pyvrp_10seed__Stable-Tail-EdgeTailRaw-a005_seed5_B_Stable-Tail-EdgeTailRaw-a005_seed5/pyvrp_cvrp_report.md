# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.0 | 0.000% | 7.819759 | 0.000% | 0.245815 | 2.541854 | 0.230130 | 0.874372 | 89.250% |
| 0.25 | 0 | 156946.7 | 6.479% | 6.665054 | 14.767% | 0.166360 | 2.258395 | 0.248110 | 0.870042 | 88.352% |
| 0.5 | 0 | 165637.0 | 12.375% | 5.212257 | 33.345% | 0.121970 | 1.724170 | 0.246418 | 0.849844 | 85.068% |
| 1 | 0 | 175928.6 | 19.357% | 3.534961 | 54.795% | 0.085744 | 1.271547 | 0.287868 | 0.816908 | 79.608% |
| 2 | 0 | 191700.9 | 30.058% | 2.761536 | 64.685% | 0.066227 | 0.921560 | 0.285247 | 0.792064 | 75.073% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

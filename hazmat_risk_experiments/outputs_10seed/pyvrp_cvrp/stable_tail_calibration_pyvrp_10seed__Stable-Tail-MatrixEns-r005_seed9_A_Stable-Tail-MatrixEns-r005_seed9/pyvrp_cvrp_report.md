# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 7.847968 | 0.000% | 0.248530 | 2.272813 | 0.165523 | 0.868834 | 89.151% |
| 0.25 | 0 | 143157.0 | 6.835% | 5.547539 | 29.312% | 0.157535 | 1.836537 | 0.235079 | 0.858268 | 87.540% |
| 0.5 | 0 | 149605.1 | 11.647% | 4.138833 | 47.262% | 0.109429 | 1.704602 | 0.296041 | 0.827896 | 83.552% |
| 1 | 0 | 158704.9 | 18.438% | 2.832928 | 63.902% | 0.065999 | 0.971318 | 0.219131 | 0.778778 | 76.542% |
| 2 | 0 | 172704.3 | 28.886% | 2.306028 | 70.616% | 0.049819 | 0.710073 | 0.231779 | 0.744025 | 71.405% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

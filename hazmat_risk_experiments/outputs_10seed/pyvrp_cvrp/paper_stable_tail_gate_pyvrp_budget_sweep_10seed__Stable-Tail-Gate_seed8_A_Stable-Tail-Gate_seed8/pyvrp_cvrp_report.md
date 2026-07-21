# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.562849 | 0.000% | 0.215845 | 2.283913 | 0.167129 | 0.860708 | 88.651% |
| 0.25 | 0 | 142725.7 | 6.514% | 6.317892 | 16.461% | 0.185105 | 1.971719 | 0.232472 | 0.857522 | 88.197% |
| 0.5 | 0 | 149154.1 | 11.311% | 4.041456 | 46.562% | 0.119008 | 1.296774 | 0.210981 | 0.819741 | 82.090% |
| 1 | 0 | 158285.2 | 18.125% | 2.894362 | 61.729% | 0.062502 | 1.007971 | 0.256053 | 0.768109 | 75.409% |
| 2 | 0 | 172964.9 | 29.081% | 2.553305 | 66.239% | 0.055907 | 0.840038 | 0.216492 | 0.745996 | 72.065% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

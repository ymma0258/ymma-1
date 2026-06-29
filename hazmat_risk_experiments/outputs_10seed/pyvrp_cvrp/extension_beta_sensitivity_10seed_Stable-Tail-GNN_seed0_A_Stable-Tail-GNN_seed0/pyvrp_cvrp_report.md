# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.576641 | 0.000% | 0.242584 | 2.483964 | 0.221180 | 0.882370 | 90.311% |
| 0.5 | 0 | 148738.8 | 11.001% | 3.992004 | 47.312% | 0.122844 | 2.081000 | 0.391020 | 0.842903 | 84.461% |
| 1 | 0 | 156818.2 | 17.031% | 2.407933 | 68.219% | 0.052249 | 0.874088 | 0.254022 | 0.789544 | 75.383% |
| 1.5 | 0 | 163384.8 | 21.931% | 2.094436 | 72.357% | 0.042257 | 0.710737 | 0.231608 | 0.754307 | 70.002% |
| 2 | 0 | 167975.9 | 25.357% | 1.667111 | 77.997% | 0.030881 | 0.468700 | 0.186878 | 0.710219 | 63.995% |
| 3 | 0 | 175985.1 | 31.335% | 1.415758 | 81.314% | 0.022881 | 0.399906 | 0.170909 | 0.660253 | 56.770% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.3 | 0.000% | 5.073533 | 0.000% | 0.160666 | 1.485284 | 0.169772 | 0.874745 | 89.424% |
| 0.25 | 0 | 142653.3 | 6.353% | 3.651496 | 28.029% | 0.105274 | 1.111077 | 0.221704 | 0.868727 | 88.312% |
| 0.5 | 0 | 148733.9 | 10.887% | 2.505108 | 50.624% | 0.073982 | 0.966753 | 0.262237 | 0.832456 | 83.049% |
| 1 | 0 | 157294.3 | 17.269% | 1.826016 | 64.009% | 0.044911 | 0.486589 | 0.124928 | 0.796303 | 77.740% |
| 2 | 0 | 171139.9 | 27.591% | 1.444232 | 71.534% | 0.029853 | 0.476758 | 0.252897 | 0.762860 | 72.450% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

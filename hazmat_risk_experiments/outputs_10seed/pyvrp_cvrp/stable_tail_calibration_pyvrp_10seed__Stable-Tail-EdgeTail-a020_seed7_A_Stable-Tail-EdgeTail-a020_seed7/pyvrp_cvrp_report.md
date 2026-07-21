# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 8.878137 | 0.000% | 0.288054 | 2.523636 | 0.171259 | 0.873752 | 89.577% |
| 0.25 | 0 | 143054.7 | 6.706% | 6.173588 | 30.463% | 0.184675 | 1.902685 | 0.217459 | 0.862063 | 87.195% |
| 0.5 | 0 | 149177.5 | 11.273% | 4.513962 | 49.156% | 0.132654 | 1.663899 | 0.278468 | 0.835605 | 83.042% |
| 1 | 0 | 158431.3 | 18.175% | 3.309906 | 62.718% | 0.090576 | 1.325616 | 0.306729 | 0.800423 | 77.642% |
| 2 | 0 | 171357.6 | 27.817% | 2.630060 | 70.376% | 0.062161 | 0.783590 | 0.222081 | 0.767104 | 72.176% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

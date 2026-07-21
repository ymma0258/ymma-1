# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.3 | 0.000% | 8.440468 | 0.000% | 0.271822 | 2.408579 | 0.168636 | 0.871541 | 89.553% |
| 0.25 | 0 | 142655.3 | 6.461% | 6.140309 | 27.252% | 0.175064 | 1.908944 | 0.205809 | 0.863763 | 88.232% |
| 0.5 | 0 | 148878.5 | 11.105% | 4.483649 | 46.879% | 0.109308 | 1.686000 | 0.254836 | 0.833138 | 84.216% |
| 1 | 0 | 157906.2 | 17.842% | 2.970141 | 64.811% | 0.066419 | 1.029046 | 0.241201 | 0.779760 | 76.631% |
| 2 | 0 | 171426.9 | 27.932% | 2.451950 | 70.950% | 0.052666 | 0.713584 | 0.220339 | 0.746745 | 71.618% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

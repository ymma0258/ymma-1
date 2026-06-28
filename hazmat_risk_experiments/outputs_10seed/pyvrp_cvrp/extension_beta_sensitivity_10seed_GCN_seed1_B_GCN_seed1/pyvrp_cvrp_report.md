# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.346082 | 0.000% | 0.261192 | 2.747818 | 0.218390 | 0.868624 | 89.353% |
| 0.5 | 0 | 165411.4 | 12.731% | 5.766785 | 30.904% | 0.148454 | 1.621567 | 0.150688 | 0.857551 | 86.545% |
| 1 | 0 | 176913.4 | 20.570% | 3.842682 | 53.958% | 0.093228 | 1.309446 | 0.303075 | 0.820139 | 80.695% |
| 1.5 | 0 | 186221.8 | 26.914% | 3.343060 | 59.945% | 0.081331 | 1.106589 | 0.270669 | 0.805469 | 78.292% |
| 2 | 0 | 194418.8 | 32.500% | 3.037228 | 63.609% | 0.070724 | 1.002364 | 0.285641 | 0.793980 | 76.437% |
| 3 | 0 | 208878.4 | 42.355% | 2.764406 | 66.878% | 0.060429 | 0.978085 | 0.297607 | 0.782099 | 74.448% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

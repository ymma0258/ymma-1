# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.8 | 0.000% | 9.070043 | 0.000% | 0.297037 | 2.702836 | 0.189515 | 0.874233 | 89.287% |
| 0.25 | 0 | 142749.5 | 6.161% | 5.870976 | 35.271% | 0.167294 | 1.900826 | 0.237104 | 0.862642 | 87.323% |
| 0.5 | 0 | 148629.2 | 10.534% | 4.713464 | 48.033% | 0.127612 | 1.547173 | 0.239282 | 0.851051 | 84.953% |
| 1 | 0 | 157762.2 | 17.326% | 3.316513 | 63.434% | 0.080288 | 1.263931 | 0.331339 | 0.813146 | 79.329% |
| 2 | 0 | 172654.1 | 28.401% | 2.911069 | 67.905% | 0.066606 | 1.195712 | 0.346060 | 0.793061 | 76.020% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

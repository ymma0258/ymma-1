# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 8.486551 | 0.000% | 0.276339 | 2.468741 | 0.175950 | 0.875863 | 89.676% |
| 0.25 | 0 | 142345.7 | 6.177% | 5.776165 | 31.937% | 0.170766 | 2.084082 | 0.294182 | 0.864602 | 87.592% |
| 0.5 | 0 | 148491.5 | 10.761% | 4.623721 | 45.517% | 0.137775 | 1.489051 | 0.224367 | 0.851238 | 84.976% |
| 1 | 0 | 157772.9 | 17.684% | 3.276525 | 61.392% | 0.084521 | 1.314603 | 0.333551 | 0.812581 | 79.221% |
| 2 | 0 | 171923.3 | 28.239% | 2.859488 | 66.306% | 0.065739 | 1.252041 | 0.359059 | 0.793083 | 76.093% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

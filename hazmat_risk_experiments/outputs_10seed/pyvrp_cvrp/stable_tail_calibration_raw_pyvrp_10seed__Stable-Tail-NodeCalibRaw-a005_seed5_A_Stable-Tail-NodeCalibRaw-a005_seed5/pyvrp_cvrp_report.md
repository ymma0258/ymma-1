# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.6 | 0.000% | 7.342380 | 0.000% | 0.223822 | 2.085707 | 0.169159 | 0.872675 | 88.879% |
| 0.25 | 0 | 142836.1 | 6.331% | 4.948972 | 32.597% | 0.140268 | 1.552272 | 0.210005 | 0.853272 | 85.681% |
| 0.5 | 0 | 148247.9 | 10.360% | 3.622718 | 50.660% | 0.104862 | 1.496580 | 0.341594 | 0.823305 | 81.307% |
| 1 | 0 | 156535.0 | 16.529% | 2.435554 | 66.829% | 0.062773 | 1.022350 | 0.318311 | 0.766120 | 72.739% |
| 2 | 0 | 168190.1 | 25.205% | 2.004872 | 72.695% | 0.044996 | 0.602977 | 0.215616 | 0.729709 | 67.437% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

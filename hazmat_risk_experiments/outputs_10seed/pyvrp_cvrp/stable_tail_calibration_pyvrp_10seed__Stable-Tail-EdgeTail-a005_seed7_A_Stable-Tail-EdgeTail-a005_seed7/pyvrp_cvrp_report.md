# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.4 | 0.000% | 8.832875 | 0.000% | 0.283657 | 2.584407 | 0.189448 | 0.874377 | 89.531% |
| 0.25 | 0 | 143168.7 | 6.738% | 5.985759 | 32.233% | 0.176395 | 1.828710 | 0.203491 | 0.859878 | 86.922% |
| 0.5 | 0 | 149424.4 | 11.402% | 4.925152 | 44.241% | 0.142596 | 2.024170 | 0.285385 | 0.842503 | 84.304% |
| 1 | 0 | 158722.8 | 18.334% | 3.205440 | 63.710% | 0.083681 | 1.241514 | 0.302486 | 0.796999 | 76.928% |
| 2 | 0 | 172682.4 | 28.741% | 2.604893 | 70.509% | 0.059704 | 0.889216 | 0.245536 | 0.764201 | 71.816% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 7.664039 | 0.000% | 0.229389 | 2.389765 | 0.214317 | 0.883567 | 90.349% |
| 0.25 | 0 | 141957.4 | 5.887% | 4.839950 | 36.849% | 0.148375 | 1.637504 | 0.249141 | 0.865848 | 86.979% |
| 0.5 | 0 | 147578.4 | 10.080% | 3.811186 | 50.272% | 0.113819 | 1.665048 | 0.324683 | 0.843238 | 84.042% |
| 1 | 0 | 155152.2 | 15.729% | 2.528582 | 67.007% | 0.062392 | 0.970350 | 0.277402 | 0.786607 | 75.806% |
| 2 | 0 | 166638.6 | 24.297% | 1.895556 | 75.267% | 0.034661 | 0.638877 | 0.246570 | 0.746867 | 69.129% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

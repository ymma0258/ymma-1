# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.7 | 0.000% | 8.830427 | 0.000% | 0.272160 | 2.477643 | 0.154993 | 0.878049 | 90.412% |
| 0.25 | 0 | 143403.5 | 7.019% | 5.801661 | 34.299% | 0.186012 | 1.822257 | 0.189596 | 0.865097 | 87.186% |
| 0.5 | 0 | 149704.7 | 11.722% | 4.645785 | 47.389% | 0.122138 | 1.603768 | 0.255499 | 0.847525 | 84.328% |
| 1 | 0 | 159247.5 | 18.843% | 3.111425 | 64.765% | 0.074142 | 0.946697 | 0.217914 | 0.806715 | 77.400% |
| 2 | 0 | 172643.9 | 28.841% | 2.269011 | 74.305% | 0.048521 | 0.802069 | 0.259019 | 0.747873 | 68.693% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.3 | 0.000% | 7.003887 | 0.000% | 0.219420 | 2.097423 | 0.166982 | 0.868500 | 88.404% |
| 0.25 | 0 | 141589.7 | 5.508% | 4.872401 | 30.433% | 0.144827 | 1.493229 | 0.207125 | 0.856598 | 86.707% |
| 0.5 | 0 | 146962.6 | 9.512% | 3.747264 | 46.497% | 0.110412 | 1.275270 | 0.238324 | 0.836051 | 83.519% |
| 1 | 0 | 155130.5 | 15.598% | 2.404459 | 65.670% | 0.063098 | 0.763088 | 0.243643 | 0.772858 | 74.527% |
| 2 | 0 | 167218.6 | 24.606% | 2.227215 | 68.200% | 0.055840 | 0.712135 | 0.256677 | 0.757879 | 72.255% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

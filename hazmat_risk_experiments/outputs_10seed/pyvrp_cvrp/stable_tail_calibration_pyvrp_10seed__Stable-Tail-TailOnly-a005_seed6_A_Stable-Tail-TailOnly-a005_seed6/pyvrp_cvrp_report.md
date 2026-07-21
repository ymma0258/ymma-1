# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134065.0 | 0.000% | 7.786350 | 0.000% | 0.227560 | 2.197324 | 0.158993 | 0.867128 | 88.782% |
| 0.25 | 0 | 143119.7 | 6.754% | 5.156710 | 33.772% | 0.146321 | 1.691256 | 0.259523 | 0.847022 | 85.477% |
| 0.5 | 0 | 149539.0 | 11.542% | 4.032796 | 48.207% | 0.116476 | 1.491268 | 0.307621 | 0.820684 | 81.816% |
| 1 | 0 | 159066.1 | 18.648% | 2.935894 | 62.294% | 0.078272 | 0.959110 | 0.256183 | 0.773956 | 75.461% |
| 2 | 0 | 173082.0 | 29.103% | 2.333945 | 70.025% | 0.054653 | 0.808131 | 0.285729 | 0.735412 | 69.967% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

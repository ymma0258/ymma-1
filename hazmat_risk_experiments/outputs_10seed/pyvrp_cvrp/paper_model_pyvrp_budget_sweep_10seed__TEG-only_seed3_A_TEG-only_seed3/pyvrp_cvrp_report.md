# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134065.1 | 0.000% | 7.784725 | 0.000% | 0.220333 | 2.532654 | 0.195395 | 0.831153 | 85.294% |
| 0.25 | 0 | 142819.8 | 6.530% | 5.431747 | 30.226% | 0.144477 | 1.599155 | 0.159484 | 0.799362 | 82.069% |
| 0.5 | 0 | 149151.6 | 11.253% | 4.553106 | 41.512% | 0.123053 | 1.579195 | 0.244554 | 0.778724 | 78.997% |
| 1 | 0 | 158583.2 | 18.288% | 3.228035 | 58.534% | 0.078718 | 0.956679 | 0.203556 | 0.699275 | 69.580% |
| 2 | 0 | 172509.2 | 28.676% | 2.825693 | 63.702% | 0.055551 | 1.053241 | 0.246822 | 0.666434 | 65.270% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

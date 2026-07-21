# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 6.337999 | 0.000% | 0.193911 | 1.843791 | 0.166090 | 0.870479 | 88.814% |
| 0.25 | 0 | 142755.7 | 6.536% | 4.526122 | 28.588% | 0.127286 | 1.447784 | 0.245918 | 0.860709 | 87.337% |
| 0.5 | 0 | 149113.0 | 11.280% | 3.276037 | 48.311% | 0.094916 | 1.290277 | 0.270881 | 0.830890 | 82.942% |
| 1 | 0 | 158110.4 | 17.995% | 2.262384 | 64.304% | 0.056957 | 0.659765 | 0.156566 | 0.786059 | 76.170% |
| 2 | 0 | 172865.1 | 29.006% | 1.835342 | 71.042% | 0.034967 | 0.558184 | 0.203661 | 0.752241 | 71.009% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

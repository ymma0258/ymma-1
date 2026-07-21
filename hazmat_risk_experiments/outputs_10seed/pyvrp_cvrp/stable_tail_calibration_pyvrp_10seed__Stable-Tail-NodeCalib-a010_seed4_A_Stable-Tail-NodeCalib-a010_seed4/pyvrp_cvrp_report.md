# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.8 | 0.000% | 8.882962 | 0.000% | 0.270027 | 2.495608 | 0.160242 | 0.879692 | 90.275% |
| 0.25 | 0 | 143232.7 | 6.838% | 6.928234 | 22.005% | 0.214550 | 2.088218 | 0.200515 | 0.874293 | 89.086% |
| 0.5 | 0 | 150033.7 | 11.911% | 5.096374 | 42.628% | 0.151070 | 1.778681 | 0.254831 | 0.855773 | 85.917% |
| 1 | 0 | 159473.5 | 18.953% | 3.569104 | 59.821% | 0.089912 | 1.169567 | 0.277471 | 0.818821 | 80.437% |
| 2 | 0 | 174365.7 | 30.061% | 2.793169 | 68.556% | 0.058161 | 1.047775 | 0.350656 | 0.788730 | 75.728% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

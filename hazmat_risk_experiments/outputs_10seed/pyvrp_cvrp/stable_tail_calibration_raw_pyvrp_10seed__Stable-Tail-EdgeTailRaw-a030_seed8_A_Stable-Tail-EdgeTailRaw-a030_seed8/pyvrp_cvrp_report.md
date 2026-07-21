# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.6 | 0.000% | 8.314021 | 0.000% | 0.269570 | 2.505729 | 0.185356 | 0.870401 | 88.784% |
| 0.25 | 0 | 142666.9 | 6.100% | 5.731653 | 31.060% | 0.162986 | 1.751295 | 0.206102 | 0.862915 | 87.471% |
| 0.5 | 0 | 148558.7 | 10.482% | 4.224627 | 49.187% | 0.126115 | 1.652487 | 0.280066 | 0.837282 | 83.634% |
| 1 | 0 | 157577.3 | 17.189% | 2.986839 | 64.075% | 0.076499 | 0.869769 | 0.184400 | 0.790411 | 77.093% |
| 2 | 0 | 171541.1 | 27.573% | 2.428570 | 70.789% | 0.052143 | 0.778682 | 0.222135 | 0.765039 | 72.753% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

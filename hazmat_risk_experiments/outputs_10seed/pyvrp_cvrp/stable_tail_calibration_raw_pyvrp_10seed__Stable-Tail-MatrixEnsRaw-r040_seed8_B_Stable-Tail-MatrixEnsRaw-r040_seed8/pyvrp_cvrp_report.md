# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 4.794364 | 0.000% | 0.148492 | 1.551138 | 0.204224 | 0.866319 | 88.595% |
| 0.25 | 0 | 156109.1 | 6.391% | 3.801468 | 20.710% | 0.088481 | 1.305956 | 0.229316 | 0.857709 | 86.994% |
| 0.5 | 0 | 164250.3 | 11.940% | 3.013481 | 37.145% | 0.073487 | 1.014053 | 0.247696 | 0.842944 | 84.321% |
| 1 | 0 | 174812.4 | 19.138% | 1.837395 | 61.676% | 0.044184 | 0.558293 | 0.181333 | 0.784901 | 75.838% |
| 2 | 0 | 188524.1 | 28.483% | 1.465037 | 69.443% | 0.031829 | 0.431394 | 0.218818 | 0.751685 | 70.546% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

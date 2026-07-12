# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 9.145129 | 0.000% | 0.283164 | 2.909357 | 0.197455 | 0.871627 | 89.165% |
| 0.25 | 0 | 158360.9 | 7.828% | 8.155028 | 10.827% | 0.205048 | 2.657839 | 0.204110 | 0.874513 | 90.217% |
| 0.5 | 0 | 169310.5 | 15.284% | 6.205470 | 32.145% | 0.157866 | 2.237107 | 0.271662 | 0.869592 | 88.035% |
| 1 | 0 | 183762.1 | 25.124% | 4.529180 | 50.474% | 0.115265 | 1.638062 | 0.344973 | 0.848322 | 83.705% |
| 2 | 0 | 206907.5 | 40.884% | 3.994634 | 56.320% | 0.100926 | 1.477861 | 0.338162 | 0.842669 | 81.838% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

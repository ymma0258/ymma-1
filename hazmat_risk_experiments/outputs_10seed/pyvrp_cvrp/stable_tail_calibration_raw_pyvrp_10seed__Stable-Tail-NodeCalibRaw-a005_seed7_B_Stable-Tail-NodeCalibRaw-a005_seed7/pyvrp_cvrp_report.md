# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.4 | 0.000% | 9.835019 | 0.000% | 0.296207 | 3.188679 | 0.212659 | 0.877154 | 90.499% |
| 0.25 | 0 | 157803.2 | 7.108% | 7.920084 | 19.471% | 0.229724 | 2.581124 | 0.229787 | 0.875522 | 89.218% |
| 0.5 | 0 | 167089.2 | 13.411% | 5.550533 | 43.564% | 0.157680 | 1.863983 | 0.240872 | 0.853333 | 84.928% |
| 1 | 0 | 178595.8 | 21.221% | 4.028033 | 59.044% | 0.104887 | 1.348921 | 0.256502 | 0.829879 | 80.528% |
| 2 | 0 | 195459.0 | 32.667% | 3.366707 | 65.768% | 0.076387 | 1.068569 | 0.224910 | 0.809016 | 77.170% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

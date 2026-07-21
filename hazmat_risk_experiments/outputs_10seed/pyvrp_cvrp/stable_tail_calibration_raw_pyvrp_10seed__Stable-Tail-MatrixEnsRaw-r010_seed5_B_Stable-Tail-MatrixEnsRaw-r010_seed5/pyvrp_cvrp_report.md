# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.5 | 0.000% | 6.961262 | 0.000% | 0.210941 | 2.302286 | 0.223666 | 0.875264 | 89.123% |
| 0.25 | 0 | 156281.5 | 6.316% | 6.184943 | 11.152% | 0.165822 | 2.045626 | 0.214364 | 0.871827 | 88.748% |
| 0.5 | 0 | 164843.3 | 12.140% | 4.344191 | 37.595% | 0.107589 | 1.392661 | 0.245541 | 0.843093 | 84.079% |
| 1 | 0 | 175253.6 | 19.222% | 3.115460 | 55.246% | 0.077076 | 1.122891 | 0.301240 | 0.818032 | 79.665% |
| 2 | 0 | 191544.7 | 30.305% | 2.485351 | 64.297% | 0.059597 | 0.808861 | 0.272392 | 0.792017 | 74.929% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `20`
- Vehicles: `4`
- Capacity: `5`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 87689.0 | 0.000% | 2.876600 | 0.000% | 0.020845 | 2.841635 | 0.743922 | 0.921308 | 100.000% |
| 0.25 | 92484.0 | 5.468% | 3.056582 | -6.257% | 0.021990 | 1.511120 | 0.383977 | 0.936503 | 100.000% |
| 0.5 | 96372.0 | 9.902% | 1.953740 | 32.082% | 0.013759 | 1.953740 | 0.750000 | 0.950060 | 100.000% |
| 1 | 101437.0 | 15.678% | 1.143908 | 60.234% | 0.007835 | 0.902877 | 0.644646 | 0.974902 | 100.000% |
| 2 | 109032.0 | 24.339% | 1.178873 | 59.019% | 0.008074 | 0.937842 | 0.647771 | 0.971154 | 100.000% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.

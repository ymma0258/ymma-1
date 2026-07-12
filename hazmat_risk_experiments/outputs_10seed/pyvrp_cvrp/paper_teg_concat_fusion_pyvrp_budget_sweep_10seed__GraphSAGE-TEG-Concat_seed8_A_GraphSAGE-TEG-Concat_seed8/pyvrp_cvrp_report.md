# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 9.513278 | 0.000% | 0.296802 | 2.600448 | 0.164227 | 0.869934 | 89.620% |
| 0.25 | 0 | 144325.7 | 7.493% | 6.075628 | 36.135% | 0.184874 | 1.954573 | 0.229432 | 0.862833 | 87.476% |
| 0.5 | 0 | 151747.6 | 13.021% | 4.609514 | 51.547% | 0.115422 | 1.389422 | 0.186024 | 0.839433 | 83.744% |
| 1 | 0 | 162066.5 | 20.707% | 3.437749 | 63.864% | 0.082721 | 1.141451 | 0.240392 | 0.810476 | 78.778% |
| 2 | 0 | 178031.2 | 32.597% | 2.519527 | 73.516% | 0.055966 | 1.005329 | 0.310753 | 0.763302 | 71.167% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
